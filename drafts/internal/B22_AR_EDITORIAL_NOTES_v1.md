# B22 Arabic Reader Draft v1 — Editorial Evidence and Review Notes

**Applies to:** `B22_AR_READER_DRAFT_v1.md` and its matched `review/B22_AR_READER_DRAFT_v1.html`
**Status:** Internal first-pass evidence layer. Unreviewed and not for publication or distribution.

## Inputs used

- `docs/ARABIC_HOUSE_STYLE_GUIDE.md` — house style, structure, safety and review rules.
- `drafts/internal/B03_AR_READER_DRAFT_v1.md` and `review/B03_AR_READER_DRAFT_v1.html` — exact model for masculine voice and HTML shell.
- `data/chapters.csv` (UTF-8 BOM), row B22 — chapter mapping, source IDs, cautions.
- `docs/BOYS_OUTLINE.md` — B22 topic set (university/training/work, faith away from home, new friendships, vocation, mentors, independent adulthood).

No other chapter files or source texts were modified.

## Scripture register — every reference `needs_verification`

| Use in reader draft | Reference | Status | Limits of use |
|---|---|---|---|
| «اتكل على الرب بكل قلبك»; paraphrase of the following clause about the Lord directing one's path | أم 3: 5–6 | `needs_verification` | Short well-known phrase only; chapter-mapped in `data/chapters.csv`. Verify Smith–Van Dyke wording, numbering and context. Applied as planning plus trust, never as "do not plan." |
| «لا يستهنّ أحد بحداثتك»; paraphrase of the charge to be an example | 1 تي 4: 12 | `needs_verification` | Short phrase; chapter-mapped. Verify wording and context (addressed to a young disciple). Used to affirm young believers, not to demand performative maturity. |

No verbatim Scripture was newly composed. Both phrases are short, referenced, and marked with `sacred-text` spans in the HTML.

## Source IDs and attributed spiritual material

| Source ID / locator | Material used | Status |
|---|---|---|
| S05 — decision-making resource, Bishop Moussa, *كيف نتخذ قرارًا*, https://st-takla.org/Full-Free-Coptic-Books/FreeCopticBooks-009-Bishop-Moussa/001-Kayfa-Atakheth-Kararan/How-to-Take-A-Decision-00-index.html | General discernment framing (ask, plan, consult) in the practical section and Q&A. | `needs_verification` — no verbatim quotation; consult chapter source record before publication. |
| S02 — البابا شنودة الثالث, *حياة الإيمان*, https://st-takla.org/Full-Free-Coptic-Books/His-Holiness-Pope-Shenouda-III-Books-Online/10-Hayat-El-Iman/Life-of-Faith_00-index.html | Mapped in `chapters.csv`; called for faith through changing contexts. | `needs_verification` — no content claim quoted in v1. |
| S12 — mapped source ID in `data/chapters.csv` | Mapped for discernment; exact work/locator to be confirmed. | `needs_verification` — no content claim taken in v1. |
| Patristic thread — St Basil on youth education, https://st-takla.org/books/adel-zekri/basil-greek-literature/text.html | Original attributed summary: forming a young person needs patient knowledge of them, not pressure into a ready-made mould. Marked `tradition-text`. | `needs_verification` — summary in our words, not a quotation; exact work, wording and rights to be confirmed. |
| S14 / M05 — student transition mental-health evidence and medical ID in `data/chapters.csv` | Only general framing: transition can bring loneliness, worry, sleep change; persistent distress should be shared with a trusted adult or professional. | `needs_verification` — no diagnosis, no prevalence figure, no clinical rule; sources not yet audited. |

## Claim and safety checks

- Opening scene is fictional; no real student or personal history is used.
- Vocations are treated respectfully: university, training, work, marriage and monasticism are all named as legitimate paths; no ranking and no universal rule.
- Local parish practice is not legislated; readers are directed to their own priest for local questions.
- No medical diagnosis. Persistent distress, sleep/appetite disruption and self-harm thoughts are routed to a trusted adult, mentor or specialist.
- Faith and prayer are presented as support alongside help, not as a replacement for it.
- No shame attached to uncertainty about the future; no claim that a "strong" believer never doubts.
- Ordinary story dialogue is not marked; only the two short verses and the attributed St Basil summary are styled in HTML.
- Local emergency and referral routes to be adapted by responsible adults before publication.

## Spiritual-thread map

| Section | Reader question | Source / influence | Bridge | Effect |
|---|---|---|---|---|
| قصة في البداية | هل أفقد إيماني حين أفقد المكان؟ | Fictional scene, none | من بطاقة طالب جديدة ورسالة ممحوحة إلى سؤال مفتوح | الأب الروحي يطرح سؤالًا ولا يحلّه → لنتحدث بصراحة |
| لنتحدث بصراحة | هل السؤال ضعف في النية؟ | None | من فقدان العادة إلى فقدان الله | «الإيمان أوسع من جدولك» → ما ينبغي أن تعرفه |
| اتكل بكل قلبك | هل التوكل بلا تخطيط؟ | أم 3: 5–6 | من الخطة المُسلَّمة إلى طريق يُقوَّم تدريجيًا | توكل عملي → لا يستهنّ أحد بحداثتك |
| لا يستهنّ أحد بحداثتك | هل صغري يُلغي شهادتي؟ | 1 تي 4: 12 | من الصدارة المُتخيَّلة إلى الأمانة اليومية | البداية بلا كمال → إيمان في مكان جديد |
| إيمان في مكان جديد | أين أصلي وأجد من يسألني؟ | S05, S14/M05 | من الغربة إلى مكان وشخص وجماعة | طلب العون عند الحاجة → طرق مختلفة |
| طرق مختلفة، رب واحد | هل يلزم قرار «كبير»؟ | St Basil summary; vocation caution | من المقارنة إلى الدعوة الخاصة | محبوب قبل القرار → إيمانك لا يتوقف على مكانك |
| إيمانك لا يتوقف على مكانك | هل الله تأخر عني؟ | Original reflection; القداس الإلهي as continuity | من الغياب المُتوهم إلى حضور سابق | مكان وشخص وخدمة → الأسئلة |
| الأسئلة | مخاوف مباشرة عن الصلاة والسخرية والدعوة والمساعدة | أم 3؛ 1 تي 4 where genuine | جواب إنساني أولًا، ثم صلة روحية | خطوة عملية |
| خطوة عملية | ماذا أفعل في مكاني الجديد؟ | Open-time invitations | من الفهم إلى خيار واحد | فكّر وصلاة |
| فكّر وصلاة | كيف أجمع هذا؟ | Original prayer | من التأمل إلى صلاة بلا اقتباس | نهاية الفصل |

## Review holds

1. **Theological/pastoral hold** — verify both chapter-mapped passages and the attributed St Basil summary; confirm the treatment of vocation and the statement that God is present in a new place.
2. **Transition/wellbeing hold** — reviewer must check the escalation language and referral path; the `S14`/`M05` evidence is not yet audited and no clinical claim may be added.
3. **Rights hold** — hosted St-Takla pages are not cleared for republication; summaries only.
4. **Language/youth hold** — confirm masculine forms, natural Arabic register and age suitability.
5. **Local-practice hold** — any statement about parish custom must be checked by the relevant pastor before publication.

## Required reviewers

- Coptic Orthodox theological reviewer / deacon (Scripture context, vocation language, patristic summary).
- Student-transition or mental-health reviewer (distress and referral wording).
- Arabic youth-language reviewer (register, masculine forms, warmth).
- Rights/copyright checker for hosted sources.
- Domain reviewer before publication, as required by `data/chapters.csv`.

## Explicit status statement

This is an **internal, unreviewed first-pass draft**. It is **not approved, not theologically cleared, and not for publication or distribution**. The unreviewed notice is retained in the HTML. All Scripture references and attributed spiritual summaries are logged as `needs_verification` above and must be checked before any further use. Markdown and HTML are synchronized; any later edit to one must be applied to the other in the same step.
