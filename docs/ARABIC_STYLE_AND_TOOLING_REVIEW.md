# Arabic-First Style and Authoring Review

**Review date:** 2026-11-07  
**Scope:** The internal Arabic B04/G05 pilot drafts and the project’s future Arabic-first
revision workflow.  
**Decision boundary:** This review proposes a house voice and tooling. It does not
approve the current drafts, copy a source author’s prose, or resolve theological,
medical, safeguarding, or rights questions.

## Executive assessment

The Arabic pilots demonstrate that the evidence/citation pipeline works. They do
not yet demonstrate a compelling youth-book voice. G05 is approximately 949
space-separated tokens including headings, source notes, and review holds; B04 is
approximately 870. The editorial target is normally 2,000–3,000 words per chapter.
The current drafts are therefore less than half the intended scale before allowing
for their visible internal apparatus.

The primary problem is not that the Arabic is incomprehensible. It is that the text
behaves like an evidence summary translated from a template:

- the opening scene resolves before a meaningful emotional or practical turn;
- explanation arrives too quickly and often sounds institutional (for example,
  “تشير مجموعة الأدلة…”);
- every section has roughly the same informational cadence;
- the direct address is correct but generic, with little lived school/family/church
  texture;
- source and reviewer language appears inside the reader-facing flow;
- the chapter has few moments of surprise, recognition, humour, dialogue, choice,
  or spiritual reflection.

## Recommended reference direction

Use **the broad pastoral qualities** of Fr. Tadros Yacoub Malaty’s *دعوني أنمو!*
as the principal tonal reference, not as a text to imitate. It is already a project
source and speaks directly to youth about dignity, growth, and the body. The relevant
section moves from a theological image to warm practical counsel addressed to the
reader. It therefore fits this project better than a purely formal doctrinal source.

The project must **not** reproduce his phrasing, imitate his personal voice, or
translate his passages without permission. Instead, build an original house voice
from these transferable qualities:

1. Start from the teenager’s real question, not a lesson objective.
2. Speak warmly and directly: “ربما…”, “تعالي نفكر…”, “لستِ وحدكِ”.
3. Move in a human sequence: scene → feeling → honest question → clear explanation
   → faith perspective → a small doable next step.
4. Let faith illuminate the experience without turning every paragraph into a sermon.
5. Use simple, living MSA—not a literal English sentence order, clinical jargon, or
   overly formal Classical Arabic.
6. Be specific about school, a trusted mother/aunt/servant, a bag, a bus, a youth
   meeting, or a private prayer, while avoiding stereotypes or invented claims.

The approved editorial policy already calls for simple, biblical, compassionate,
practical, original prose inspired by general qualities associated with Pope Shenouda
III—not impersonation. This recommendation follows the same constraint.

## Arabic house-voice specification

### Reader and register

- Reader: a Coptic Orthodox teenager, approximately 12–18, in Egypt or diaspora.
- Register: **الفصحى المبسطة** that sounds spoken when read aloud, while remaining
  dignified and understandable across Arabic-speaking communities.
- Relationship: a trustworthy older sister/brother or wise servant speaking *with*
  the reader, never lecturing *at* her or him.
- Pronouns: maintain chapter-appropriate gender without constant repetition of
  “أنتِ/أنت”. Use the reader’s name in scenes, then natural direct address.

### Sentence and paragraph rhythm

- Prefer a mixture of short reassuring sentences and medium-length explanatory
  sentences. Break long chains of clauses.
- Give each paragraph one emotional or practical job.
- Follow a factual paragraph with a human sentence: “وقد يربككِ هذا، وهذا مفهوم.”
- Replace abstract labels with a concrete effect whenever possible. Rather than
  “قد تواجهين مشاعر متباينة”، write “قد تشعرين بالحرج في المدرسة، أو بالقلق لأنك
  لا تعرفين ما الذي ستفعلينه.”
- Do not repeat “من الطبيعي” as a reflex. Explain *what* may be normal, then make
  room for uncertainty and help-seeking.

### Chapter architecture for a full Arabic pilot

1. **افتتاح قصصي (250–350 كلمة):** a plausible scene with a small complication,
   inner thought, safe adult response, and unresolved question that pulls the reader
   forward.
2. **لنتحدث بصراحة:** name the awkward question plainly and kindly.
3. **ما ينبغي أن تعرفيه/تعرفه:** medically bounded explanation in short units,
   examples, and a calm “متى أطلب مساعدة؟” box.
4. **جسدي له كرامة:** original pastoral synthesis supported by the evidence brief;
   no imitation or unverified quotation.
5. **أسئلة قد تخجلين من طرحها:** 4–6 candid Q&As with varied answer shapes.
6. **خطوات صغيرة لهذا الأسبوع:** a choice, not a command list.
7. **مساحة للصلاة والتفكير:** original prayer, reflection, and safe support prompt.
8. **Internal notes only:** citations, review holds, and source details must live in
   a separate reviewer layer or footnotes, not interrupt a youth reader’s page.

## Example: improving the opening without copying a source

The present G05 opening states the situation efficiently, but it ends before the
reader can inhabit it. A stronger *original* opening should let the moment breathe:

> كان جرس الحصة الثانية قد رنّ، ومريم ما زالت تحدّق في دفترها من غير أن تقرأ
> سطرًا واحدًا. لم تكن تعرف كيف تطلب المساعدة، ولا كيف تنهض من مقعدها من غير أن
> يلاحظ أحد. ثم تذكرت ما قالته لها أمها مرة: “إذا حدث شيء لا تفهمينه، لا تحمليه
> وحدكِ.” رفعت يدها ببطء. لم تحلّ كل أسئلتها في تلك اللحظة، لكن شيئًا واحدًا تغيّر:
> لم تعد تخاف أن تسأل.

This works because it supplies a sensory moment, an inner thought, a safe response,
and a reason to keep reading. It does **not** introduce a medical claim or imitate a
protected author.

## What to remove from the reader version

Move the following to an internal review layer:

- `[CLM:…]` evidence markers;
- `[REVIEW-NEEDED: …]` blocks;
- phrases such as “مصدر رعوي في قاعدة الأدلة” and “مجموعة الأدلة المؤهلة”;
- source lists and pipeline status notes.

The reader version may retain a short, human references page after review. The
evidence trace must remain available to editors, but it should not break the
experience of a teenager reading a chapter.

## Recommended authoring and review stack

| Need | Recommended component | Role and limit |
|---|---|---|
| Evidence safety | Existing `writing_system/workflow.py` and claim IDs | Keep this as the factual/theological boundary. It validates registered IDs only; it cannot judge whether Arabic feels alive. |
| Arabic house style | New project-local `arabic-youth-authoring` skill or style guide | Store voice principles, forbidden boilerplate, chapter beats, term glossary, and before/after examples. This is the highest-value addition. |
| Consistency linting | [Vale](https://vale.sh/) with custom project rules | Use custom rules for banned boilerplate, inconsistent Church terminology, overused transitions, headings, and visible internal markers. Vale enforces a chosen style; it does not create good prose by itself. |
| Arabic spelling/grammar pass | [LanguageTool Arabic support](https://help.languagetool.org/hc/en-us/articles/39254526141463-What-languages-does-LanguageTool-support) | Use as a mechanical pass, then accept/reject suggestions with a native Arabic editor. It is not a youth-voice evaluator. |
| Arabic normalization and morphology | [CAMeL Tools](https://camel-tools.readthedocs.io/) | Useful for normalization, tokenization, morphology, and terminology checks. It will not tell whether a scene is moving or pastorally appropriate. |
| AI drafting discipline | [OpenAI prompt engineering guidance](https://developers.openai.com/api/docs/guides/prompt-engineering) and [evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Give the authoring model a concise Arabic house style plus 2–3 original approved examples; require a structured self-check. Maintain human-scored examples/evals rather than relying on “sounds good.” |
| Review UI | Existing trilingual HTML review viewer | Make Arabic the default, but add a reviewer-only toggle so citations/holds can be hidden when judging readability and shown when judging evidence. |

## Repositories and configurations worth reusing

1. [Vale CLI](https://github.com/vale-cli/vale) is the best fit for a repository
   workflow because rules live with the manuscript and can run in CI. Start with a
   tiny custom Arabic ruleset rather than importing an English style guide.
2. [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) is a credible open-source
   Arabic NLP foundation for normalization, morphology, and terminology checks.
3. Do **not** adopt `proselint` for the Arabic core: it is primarily an English prose
   linter. It can still help English adaptations later.

## Minimal automated Arabic checks to add

- Flag reader-facing `CLM:` and `REVIEW-NEEDED:` markers.
- Flag repeated boilerplate within one chapter: “من الطبيعي”، “من المهم”، “تجدر
  الإشارة”، “في هذا الفصل”، “تشير الأدلة”.
- Flag three consecutive paragraphs beginning with the same connector.
- Require one scene, at least four reader questions, one specific safe-action choice,
  and an original prayer.
- Report average paragraph length and the number of direct questions; use these as
  prompts for human revision, not hard quality scores.
- Maintain an Arabic Coptic glossary: e.g., القداس الإلهي، التناول، الاعتراف، الأب
  الروحي، النعمة، التوبة. Each change must propagate to English/German review.

## Proposed next writing workflow

1. Create the Arabic style guide/skill and a 10-item editorial scorecard.
2. Re-outline G05 in Arabic to approximately 2,000–2,500 words before rewriting
   prose. Add scene beats, questions, practical situations, and reflection beats.
3. Rewrite only the Arabic reader layer; keep the evidence/review layer separate.
4. Run terminology/boilerplate checks and a native-Arabic “read aloud” pass.
5. Score the rewrite against the rubric: warmth, specificity, youth pull, clarity,
   evidence boundaries, safeguarding tone, and Coptic pastoral fit.
6. Once Arabic is editorially stable, reconcile—not mechanically translate—the
   English and German drafts.

## Recommendation

Do not patch the existing Arabic wording sentence by sentence. Treat G05 as the
first **full Arabic house-style rewrite** and use it to establish the reusable voice
for the book. The correct immediate deliverable is a style guide plus an Arabic
chapter outline/beat sheet; the full rewrite should follow only after those are
approved.
