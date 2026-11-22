import pathlib,sqlite3,tempfile,unittest,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from kb1_upgrade import upgrade,counts
from kb1_readiness import report

class KB1Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.src=pathlib.Path(self.tmp.name)/"source.sqlite"
        self.dst=pathlib.Path(self.tmp.name)/"migrated.sqlite"
        with sqlite3.connect(self.src) as db:
            for name in ("chapters","works","sources","passages","claims","evidence","chapter_claims","reviews","translations","phase2_source_discovery"):
                db.execute(f'CREATE TABLE "{name}"(id TEXT)')
                db.execute(f'INSERT INTO "{name}" VALUES (?)',("original",))
    def test_requires_actual_project_schema(self):
        with self.assertRaises(Exception): upgrade(self.src,self.dst)
        self.assertFalse(self.dst.exists())
    def test_refuses_overwrite(self):
        self.dst.write_text("keep")
        with self.assertRaises(FileExistsError): upgrade(self.src,self.dst)
        self.assertEqual(self.dst.read_text(),"keep")
    def test_refuses_inplace(self):
        with self.assertRaises(ValueError): upgrade(self.src,self.src)

if __name__=="__main__":unittest.main()
