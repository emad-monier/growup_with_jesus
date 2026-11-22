# B23 Arabic Reader Draft v1 — Editorial Evidence and Review Notes

**Applies to:** `B23_AR_READER_DRAFT_v1.md` and its matched `review/B23_AR_READER_DRAFT_v1.html`
**Status:** Internal first-pass evidence layer. Unreviewed and not for publication or distribution.

## Inputs used

- `docs/ARABIC_HOUSE_STYLE_GUIDE.md` — house style, structure, safety and review rules.
- `drafts/internal/B03_AR_READER_DRAFT_v1.md` and `review/B03_AR_READER_DRAFT_v1.html` — exact model for masculine voice and HTML shell.
- `data/chapters.csv` (UTF-8 BOM), row B23 — chapter mapping, source IDs, cautions.
- `docs/BOYS_OUTLINE.md` — B23 topic set (future self, core values, spiritual/personal/educational goals, prayer, trusted support, growth plan).

No other chapter files or source texts were modified. The editorial caution "do not impose rigid spiritual disciplines" is treated as a binding constraint for this draft.

## Scripture register — every reference `needs_verification`

| Use in reader draft | Reference | Status | Limits of use |
|---|---|---|---|
| «أضيفوا إلى إيمانكم فضيلة»; paraphrase of the list of added virtues | 2 بط 1: 5–8 | `needs_verification` | Short phrase only; chapter-mapped in `data/chapters.csv`. Verify Smith–Van Dyke wording, numbering and context. Applied as gradual addition, never as a scorecard or a test of whether someone is a real believer. |
| «ينسى ما وراء ويمتدّ إلى قدّام»; paraphrase of pressing toward the goal | فل 3: 12–14 | `needs_verification` | Short phrase used twice, with the reference; chapter-mapped. Verify wording and context (the speaker says he has not yet attained). Applied as returning after failure, not as comparing oneself with others. |

No verbatim Scripture was newly composed. Both phrases are short, referenced, and marked with `sacred-text` spans in the HTML.

## Source IDs and attributed spiritual material

| Source ID / locator | Material used | Status |
|---|---|---|
| S02 — البابا شنودة الثالث, *حياة الإيمان*, https://st-takla.org/Full-Free-Coptic-Books/His-Holiness-Pope-Shenouda-III-Books-Online/10-Hayat-El-Iman/Life-of-Faith_00-index.html | Mapped in `chapters.csv`; called for inner life and growth. | `needs_verification` — no verbatim content claim taken in v1. |
| S11 — mapped source ID in `data/chapters.csv` | Mapped for personal rule of life; exact work/locator to be confirmed. | `needs_verification` — no content claim taken in v1. |
| S05 — decision-making resource, Bishop Moussa, *كيف نتخذ قرارًا*, https://st-takla.org/Full-Free-Coptic-Books/FreeCopticBooks-009-Bishop-Moussa/001-Kayfa-Atakheth-Kararan/How-to-Take-A-Decision-00-index.html | General framing for reconsidering a rule when circumstances change. | `needs_verification` — no verbatim quotation. |
| الأب تادرس يعقوب ملطي, *دعوني أنمو!* (soul chapter), https://st-takla.org/books/fr-tadros-malaty/grow/soul.html | Original attributed summary: growth of the soul is gradual and not measured by a single day; adolescence is a time of building, not accusation. Marked `tradition-text`. | `needs_verification` — summary in our words, not a quotation; hosted text not cleared for republication. |
| Patristic thread — St Anthony sayings | Listed in `data/chapters.csv` as "sayings pending." | `needs_verification` — no saying attributed from memory; excluded from v1 reader copy. |
| Goal-setting evidence (editorial requirement in `data/chapters.csv`) | No external goal-setting claim or figure used; only open-time, small-step suggestions. | `needs_verification` — specialist review needed before any evidence-based claim is added. |
| M05 — medical ID in `data/chapters.csv` | No medical claim; sources not audited. | `needs_verification` — any later health-related statement requires specialist review. |

## Claim and safety checks

- Opening scene is fictional; no real minor or personal history is used.
- **Spiritual-discipline caution:** no rigid rule is imposed, no universal count of prayers or fasting practice is given, and no local Church rule is invented. The reader is told to adapt a rule to age, health, school and family circumstances.
- The Coptic term is rendered as «الأجبية»; no claim is made that a particular number of prayers is required. Local questions are referred to the father of confession or priest.
- If a practice causes persistent distress, harms sleep, eating or study, or becomes compulsive, the text directs the reader to a trusted adult and, if needed, a specialist. No diagnosis is made and no "spiritual" explanation is substituted for care.
- No shame: missed days, tiredness and rest are not called weak faith; returning is treated as the practice itself.
- Faith is support alongside help, never a replacement for it. Local referral and emergency routes to be adapted by responsible adults before publication.
- Ordinary story dialogue is not marked; only the two short verses and the attributed Fr Tadros summary are styled in HTML.

## Spiritual-thread map

| Section | Reader question | Source / influence | Bridge | Effect |
|---|---|---|---|---|
| قصة في البداية | هل أنا كسول أم أن الصفحة هي المشكلة؟ | Fictional scene, none | من دفتر ومربعات فارغة إلى سؤال مفتوح | الأب الروحي يقول «قليل صادق خير من كثير متخيّل» → لنتحدث بصراحة |
| لنتحدث بصراحة | هل الترتيب امتحان أم وسيلة؟ | None | من تعنيف النفس إلى إعادة النظر في الطريقة | القاعدة ليست حملًا → ما ينبغي أن تعرفه |
| أضف، لا تُحاسِ نفسك | هل النمو قفزة تُحاسَب؟ | 2 بط 1: 5–8 | من الإتقان إلى الإضافة التدريجية | خطوات صغيرة تُضاف → أنسى ما وراء |
| أنسى ما وراء وأمتدّ إلى قدّام | هل خطأ الأمس حكم عليّ؟ | فل 3: 12–14 | من الحساب إلى العودة بلا لوم | «ما مضى لا يُلغي اليوم» → قاعدة بلا قسوة |
| قاعدة بلا قسوة | هل أُجبر جسدي على قالب؟ | Spiritual-discipline caution; M05 | من الصرامة إلى الموازنة | بالغ موثوق عند الحاجة → كلمة الآباء |
| كلمة الآباء | هل يُقاس النمو بيوم واحد؟ | Fr Tadros Malaty, attributed summary | من المربعات إلى التدرّج | الترتيب وسيلة → قاعدتك تشبهك |
| قاعدتك تشبهك | هل قاعدتي تُقرّبني أم تُعاقبني؟ | Original reflection; الاعتراف as mercy | من الأداء إلى الكرامة والراحة | أسئلة الفحص → الأسئلة |
| الأسئلة | مخاوف مباشرة عن الأجبية والكسر والمقارنة والتغيير والمساعدة | 2 بط؛ فل where genuine | جواب إنساني أولًا، ثم صلة روحية | خطوة عملية |
| خطوة عملية | من أين أبدأ اليوم؟ | Open-time invitations | من الفهم إلى خطوة واحدة | فكّر وصلاة |
| فكّر وصلاة | كيف أجمع هذا؟ | Original prayer | من التأمل إلى صلاة بلا اقتباس | نهاية الفصل |

## Review holds

1. **Theological/pastoral hold (mandatory)** — verify both chapter-mapped passages, the attributed Fr Tadros summary, and the whole treatment of spiritual discipline. Confirm that no reader could infer a required number of prayers, a binding fast, or a universal Church rule.
2. **Safeguarding/wellbeing hold** — review the compulsion/distress escalation wording and referral path; `M05` evidence is not audited and no clinical claim may be added.
3. **Rights hold** — hosted St-Takla and Fr Tadros material is not cleared for republication; summaries only.
4. **Language/youth hold** — confirm masculine forms, natural Arabic register, and the use of «الأجبية» as the house term.
5. **St Anthony hold** — sayings remain pending; do not insert an attributed saying from memory in a later pass without verification.

## Required reviewers

- Coptic Orthodox theological reviewer / deacon (Scripture context, spiritual-discipline guidance, terminology).
- Father of confession or pastoral adviser (rule-of-life language and local practice).
- Mental-health or wellbeing reviewer (distress/compulsion escalation and referral).
- Arabic youth-language reviewer (register, masculine forms, warmth).
- Rights/copyright checker for hosted sources.
- Specialist reviewer before publication, as required by `data/chapters.csv`.

## Explicit status statement

This is an **internal, unreviewed first-pass draft**. It is **not approved, not theologically cleared, and not for publication or distribution**. The unreviewed notice is retained in the HTML. All Scripture references, the attributed spiritual summary, and the pending patristic material are logged as `needs_verification` above and must be checked before any further use. Markdown and HTML are synchronized; any later edit to one must be applied to the other in the same step.
