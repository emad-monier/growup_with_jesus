import tempfile,unittest,pathlib
import workflow

class WorkflowTests(unittest.TestCase):
    def test_b04_brief(self):
        result=workflow.brief("B04")
        self.assertTrue(result["grounded_claims"])
        self.assertEqual(result["evidence_class"],"source_checked_not_expert_approved")

    def test_g05_pastoral_hold(self):
        result=workflow.brief("G05")
        self.assertTrue(any("Communion" in warning for warning in result["editorial_warnings"]))

    def test_invented_citation_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            draft=pathlib.Path(directory)/"draft.md"
            draft.write_text("## Understanding the topic\n## What our Church teaches\n## Practical advice\n[CLM:INVENTED]",encoding="utf-8")
            result=workflow.check("B04",draft)
            self.assertIn("INVENTED",result["invalid_citations"])
            self.assertFalse(result["publication_approved"])

if __name__=="__main__":
    unittest.main()
