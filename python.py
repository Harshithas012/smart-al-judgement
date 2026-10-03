from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# =========================
# LEGAL CASE DATABASE
# =========================

legalCases = [

    {
        "id": 1,
        "case": "Murder",
        "keywords": [
            "murder",
            "killed",
            "intentionally killed",
            "shot and killed"
        ],
        "offenceSection": "BNS Section 101",
        "punishmentSection": "BNS Section 103",
        "punishment": "Death or imprisonment for life and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Post-mortem report",
            "CCTV",
            "Witness statements",
            "Forensic evidence",
            "Weapon"
        ],
        "explanation": "The facts may indicate murder if the legal requirements for murder are established."
    },

    {
        "id": 2,
        "case": "Murder by a life-convict",
        "keywords": [
            "life convict murder",
            "prisoner killed",
            "life prisoner commits murder"
        ],
        "offenceSection": "BNS Section 101",
        "punishmentSection": "BNS Section 104",
        "punishment": "Death or imprisonment for life for the remainder of natural life",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Prison records",
            "Witness statements",
            "Medical evidence",
            "CCTV"
        ],
        "explanation": "A murder committed by a person already serving a life sentence can attract the special punishment provision."
    },

    {
        "id": 3,
        "case": "Culpable homicide",
        "keywords": [
            "culpable homicide",
            "caused death",
            "death without murder"
        ],
        "offenceSection": "BNS Section 100",
        "punishmentSection": "BNS Section 105",
        "punishment": "Punishment depends on whether there was intention or knowledge",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Medical report",
            "Witness statements",
            "Forensic evidence"
        ],
        "explanation": "The facts may amount to culpable homicide where the legal requirements are established but the case does not amount to murder."
    },

    {
        "id": 4,
        "case": "Death caused by negligence",
        "keywords": [
            "negligent death",
            "death due to negligence",
            "negligent act caused death"
        ],
        "offenceSection": "BNS Section 106",
        "punishmentSection": "BNS Section 106",
        "punishment": "Up to 5 years and fine, subject to the applicable subsection",
        "classification": "Cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": [
            "Medical records",
            "Expert evidence",
            "Witness statements",
            "CCTV"
        ],
        "explanation": "A death caused by a negligent act may fall under the applicable provision of Section 106."
    },

    {
        "id": 5,
        "case": "Attempt to murder",
        "keywords": [
            "attempted murder",
            "tried to kill",
            "shot but survived",
            "stabbed to kill"
        ],
        "offenceSection": "BNS Section 109",
        "punishmentSection": "BNS Section 109",
        "punishment": "Up to 10 years and fine; if hurt is caused, imprisonment for life may apply",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Weapon",
            "Medical report",
            "CCTV",
            "Witness statements",
            "Forensic evidence"
        ],
        "explanation": "The facts may indicate attempt to murder where the required intention and acts are established."
    },

    {
        "id": 6,
        "case": "Attempt to commit culpable homicide",
        "keywords": [
            "attempt culpable homicide",
            "attempted killing",
            "caused injury during attempted killing"
        ],
        "offenceSection": "BNS Section 110",
        "punishmentSection": "BNS Section 110",
        "punishment": "Up to 3 years; if hurt is caused, up to 7 years",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Medical report",
            "Weapon",
            "Witness statements"
        ],
        "explanation": "The applicable punishment depends on whether hurt was caused."
    },

    {
        "id": 7,
        "case": "Abetment of suicide",
        "keywords": [
            "suicide",
            "encouraged suicide",
            "instigated suicide",
            "forced suicide"
        ],
        "offenceSection": "BNS Section 108",
        "punishmentSection": "BNS Section 108",
        "punishment": "Up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Messages",
            "Witness statements",
            "Suicide note",
            "Call records"
        ],
        "explanation": "Evidence must establish the legally required conduct amounting to abetment."
    },

    {
        "id": 8,
        "case": "Abetment of suicide of child or person of unsound mind",
        "keywords": [
            "child suicide",
            "suicide of child",
            "instigated child suicide"
        ],
        "offenceSection": "BNS Section 107",
        "punishmentSection": "BNS Section 107",
        "punishment": "Death, life imprisonment, or imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Messages",
            "Witness statements",
            "Digital evidence",
            "Medical records"
        ],
        "explanation": "Section 107 applies to the specified protected categories when its legal requirements are established."
    },

    {
        "id": 9,
        "case": "Kidnapping",
        "keywords": [
            "kidnapped",
            "kidnap",
            "taken away",
            "abducted"
        ],
        "offenceSection": "BNS Section 137",
        "punishmentSection": "BNS Section 137(2)",
        "punishment": "Up to 7 years and fine",
        "classification": "Cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": [
            "CCTV",
            "Phone location",
            "Witness statements",
            "Travel records"
        ],
        "explanation": "The facts may constitute kidnapping if the legal requirements are satisfied."
    },

    {
        "id": 10,
        "case": "Kidnapping for begging",
        "keywords": [
            "child begging",
            "kidnap child for begging",
            "force child to beg"
        ],
        "offenceSection": "BNS Section 139(1)",
        "punishmentSection": "BNS Section 139(1)",
        "punishment": "Rigorous imprisonment of at least 10 years up to life imprisonment and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": [
            "Child statement",
            "Witness statements",
            "CCTV",
            "Medical evidence"
        ],
        "explanation": "The provision applies where a child is kidnapped for the purpose of begging."
    },

    {
        "id": 11,
        "case": "Maiming a child for begging",
        "keywords": [
            "maimed child",
            "injured child for begging",
            "disabled child for begging"
        ],
        "offenceSection": "BNS Section 139(2)",
        "punishmentSection": "BNS Section 139(2)",
        "punishment": "At least 20 years imprisonment up to the remainder of natural life and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Medical report",
            "Child statement",
            "Witnesses",
            "CCTV"
        ],
        "explanation": "The provision addresses maiming a child for the purpose of begging."
    },

    {
        "id": 12,
        "case": "Kidnapping to murder",
        "keywords": [
            "kidnap to kill",
            "kidnapped for murder",
            "abducted to murder"
        ],
        "offenceSection": "BNS Section 140(1)",
        "punishmentSection": "BNS Section 140(1)",
        "punishment": "Life imprisonment or rigorous imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "CCTV",
            "Phone records",
            "Witness statements",
            "Forensic evidence"
        ],
        "explanation": "The provision applies where kidnapping or abduction is connected with the intention to murder."
    },

    {
        "id": 13,
        "case": "Kidnapping for ransom",
        "keywords": [
            "ransom",
            "kidnap for money",
            "money demanded for release"
        ],
        "offenceSection": "BNS Section 140(2)",
        "punishmentSection": "BNS Section 140(2)",
        "punishment": "Death or imprisonment for life and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Ransom messages",
            "Call records",
            "Bank records",
            "CCTV"
        ],
        "explanation": "Kidnapping or abduction for ransom is covered by the specified provision."
    },

    {
        "id": 14,
        "case": "Kidnapping for secret confinement",
        "keywords": [
            "kidnap and confine",
            "secret confinement",
            "abducted and locked"
        ],
        "offenceSection": "BNS Section 140(3)",
        "punishmentSection": "BNS Section 140(3)",
        "punishment": "Up to 7 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": [
            "CCTV",
            "Location records",
            "Victim statement",
            "Witness statements"
        ],
        "explanation": "The provision applies where kidnapping or abduction is intended to secretly and wrongfully confine a person."
    },

    {
        "id": 15,
        "case": "Kidnapping to cause grievous hurt",
        "keywords": [
            "kidnap to injure",
            "abduct for grievous hurt",
            "kidnap and seriously injure"
        ],
        "offenceSection": "BNS Section 140(4)",
        "punishmentSection": "BNS Section 140(4)",
        "punishment": "Up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Medical report",
            "Victim statement",
            "CCTV",
            "Weapon evidence"
        ],
        "explanation": "The provision covers specified kidnapping or abduction intended to subject a person to grievous hurt or other listed harm."
    },

    {
        "id": 16,
        "case": "Assault on woman with intent to outrage modesty",
        "keywords": [
            "assault woman",
            "attack woman",
            "outrage modesty",
            "force against woman"
        ],
        "offenceSection": "BNS Section 74",
        "punishmentSection": "BNS Section 74",
        "punishment": "1 to 5 years imprisonment and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": [
            "Victim statement",
            "CCTV",
            "Witness statements",
            "Medical report"
        ],
        "explanation": "The facts may fall under Section 74 where the required intention and use of assault or criminal force are established."
    },

    {
        "id": 17,
        "case": "Sexual harassment",
        "keywords": [
            "sexual harassment",
            "unwanted sexual conduct",
            "sexual remarks",
            "unwanted advances"
        ],
        "offenceSection": "BNS Section 75",
        "punishmentSection": "BNS Section 75",
        "punishment": "Punishment depends on the particular act covered by the subsection",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Messages",
            "Emails",
            "Witness statements",
            "CCTV"
        ],
        "explanation": "The exact punishment depends on which form of sexual harassment is established."
    },

    {
        "id": 18,
        "case": "Assault with intent to disrobe",
        "keywords": [
            "disrobe woman",
            "remove clothes by force",
            "attempt to undress"
        ],
        "offenceSection": "BNS Section 76",
        "punishmentSection": "BNS Section 76",
        "punishment": "3 to 7 years imprisonment and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Victim statement",
            "CCTV",
            "Witnesses",
            "Medical evidence"
        ],
        "explanation": "Section 76 concerns assault or criminal force with the specified intention to disrobe."
    },

    {
        "id": 19,
        "case": "Voyeurism",
        "keywords": [
            "voyeurism",
            "secret recording",
            "private image",
            "recorded woman secretly"
        ],
        "offenceSection": "BNS Section 77",
        "punishmentSection": "BNS Section 77",
        "punishment": "Punishment depends on whether it is a first or subsequent conviction",
        "classification": "Cognizable",
        "court": "Court of Session",
        "evidence": [
            "Phone",
            "Video",
            "Cloud records",
            "Digital forensic evidence"
        ],
        "explanation": "Secretly watching, capturing or disseminating an image of a woman in circumstances covered by the provision may constitute voyeurism."
    },

    {
        "id": 20,
        "case": "Stalking",
        "keywords": [
            "stalking",
            "following woman",
            "repeated contact",
            "online stalking"
        ],
        "offenceSection": "BNS Section 78",
        "punishmentSection": "BNS Section 78",
        "punishment": "Up to 3 years and fine for the specified first offence",
        "classification": "Cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": [
            "Call records",
            "Messages",
            "Social media records",
            "CCTV"
        ],
        "explanation": "Repeated following, contacting or monitoring may fall under stalking when the statutory requirements are met."
    },

    {
        "id": 21,
        "case": "Dowry death",
        "keywords": [
            "dowry death",
            "dowry harassment death",
            "wife died because of dowry"
        ],
        "offenceSection": "BNS Section 80",
        "punishmentSection": "BNS Section 80",
        "punishment": "At least 7 years imprisonment up to life imprisonment",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Post-mortem report",
            "Dowry records",
            "Messages",
            "Witness statements"
        ],
        "explanation": "A death meeting the statutory dowry-death requirements may attract Section 80."
    },

    {
        "id": 22,
        "case": "Cruelty by husband or relative",
        "keywords": [
            "husband cruelty",
            "wife harassment",
            "in-laws harassment",
            "domestic cruelty"
        ],
        "offenceSection": "BNS Section 85",
        "punishmentSection": "BNS Section 85",
        "punishment": "Up to 3 years and fine",
        "classification": "See applicable BNSS classification",
        "court": "Magistrate",
        "evidence": [
            "Messages",
            "Witness statements",
            "Medical records",
            "Complaint records"
        ],
        "explanation": "Cruelty by a husband or relative may fall under Section 85 when the statutory definition is satisfied."
    },

    {
        "id": 23,
        "case": "Causing miscarriage",
        "keywords": [
            "miscarriage",
            "caused miscarriage",
            "illegal abortion"
        ],
        "offenceSection": "BNS Section 88",
        "punishmentSection": "BNS Section 88",
        "punishment": "Punishment depends on the circumstances and applicable subsection",
        "classification": "See applicable BNSS classification",
        "court": "Magistrate of the First Class",
        "evidence": [
            "Medical records",
            "Doctor report",
            "Witness statements"
        ],
        "explanation": "The legal provision applies subject to its statutory exceptions and requirements."
    },

    {
        "id": 24,
        "case": "Causing miscarriage without consent",
        "keywords": [
            "forced abortion",
            "miscarriage without consent",
            "abortion without consent"
        ],
        "offenceSection": "BNS Section 89",
        "punishmentSection": "BNS Section 89",
        "punishment": "Life imprisonment or up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": [
            "Medical records",
            "Victim statement",
            "Witness statements",
            "Messages"
        ],
        "explanation": "Causing miscarriage without the woman's consent is specifically addressed by Section 89."
    },

    {
        "id": 25,
        "case": "Abandonment of child",
        "keywords": [
            "abandoned child",
            "left baby",
            "abandon baby",
            "child abandoned"
        ],
        "offenceSection": "BNS Section 93",
        "punishmentSection": "BNS Section 93",
        "punishment": "Up to 7 years, or fine, or both",
        "classification": "Cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": [
            "CCTV",
            "Witness statements",
            "Hospital records",
            "Child protection records"
        ],
        "explanation": "Abandoning a child under the circumstances specified by Section 93 may constitute the offence."
    },
    # 26
    {
        "id": 26,
        "case": "Cohabitation by deceitful belief of lawful marriage",
        "keywords": ["fake marriage", "false marriage", "deceitful marriage", "lawful marriage"],
        "offenceSection": "BNS Section 81",
        "punishmentSection": "BNS Section 81",
        "punishment": "Imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Marriage-related documents", "Messages", "Witness statements", "Communication records"]
    },

    # 27
    {
        "id": 27,
        "case": "Marrying again during lifetime of husband or wife",
        "keywords": ["second marriage", "bigamy", "married again", "two marriages"],
        "offenceSection": "BNS Section 82",
        "punishmentSection": "BNS Section 82",
        "punishment": "Imprisonment up to 7 years and fine",
        "classification": "See applicable BNSS classification",
        "court": "Magistrate",
        "evidence": ["Marriage certificate", "Marriage photographs", "Witness statements", "Marriage records"]
    },

    # 28
    {
        "id": 28,
        "case": "Fraudulent marriage ceremony without lawful marriage",
        "keywords": ["fake marriage ceremony", "fraud marriage", "marriage ceremony", "false marriage"],
        "offenceSection": "BNS Section 83",
        "punishmentSection": "BNS Section 83",
        "punishment": "Imprisonment up to 7 years and fine",
        "classification": "See applicable BNSS classification",
        "court": "Magistrate",
        "evidence": ["Ceremony records", "Photographs", "Videos", "Witness statements"]
    },

    # 29
    {
        "id": 29,
        "case": "Death caused while attempting to cause miscarriage",
        "keywords": ["miscarriage death", "death during abortion", "causing miscarriage death"],
        "offenceSection": "BNS Section 90",
        "punishmentSection": "BNS Section 90",
        "punishment": "Up to 10 years and fine; without consent, life imprisonment or the specified punishment",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Medical records", "Post-mortem report", "Doctor evidence", "Witness statements"]
    },

    # 30
    {
        "id": 30,
        "case": "Act intended to prevent child being born alive",
        "keywords": ["prevent child birth", "child not born alive", "death after birth", "unborn child"],
        "offenceSection": "BNS Section 91",
        "punishmentSection": "BNS Section 91",
        "punishment": "Imprisonment up to 10 years, or fine, or both",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Medical records", "Medical expert opinion", "Witness statements", "Forensic evidence"]
    },

    # 31
    {
        "id": 31,
        "case": "Causing death of quick unborn child",
        "keywords": ["unborn child death", "quick unborn child", "culpable homicide unborn child"],
        "offenceSection": "BNS Section 92",
        "punishmentSection": "BNS Section 92",
        "punishment": "Imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Medical evidence", "Post-mortem/medical examination", "Witness statements", "Forensic evidence"]
    },

    # 32
    {
        "id": 32,
        "case": "Exposure or abandonment of child",
        "keywords": ["abandon child", "leave child", "abandoned child", "child abandonment"],
        "offenceSection": "BNS Section 93",
        "punishmentSection": "BNS Section 93",
        "punishment": "Imprisonment up to 7 years, or fine, or both",
        "classification": "Cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Child protection records", "Witness statements", "CCTV", "Medical records"]
    },

    # 33
    {
        "id": 33,
        "case": "Concealment of birth by secret disposal of dead body",
        "keywords": ["conceal birth", "dead newborn", "secret disposal", "hide birth"],
        "offenceSection": "BNS Section 94",
        "punishmentSection": "BNS Section 94",
        "punishment": "Imprisonment up to 2 years, or fine, or both",
        "classification": "Cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Medical records", "Dead body examination", "Witness statements", "Forensic evidence"]
    },

    # 34
    {
        "id": 34,
        "case": "Hiring or using a child to commit an offence",
        "keywords": ["child used in crime", "hire child", "employ child crime", "child criminal activity"],
        "offenceSection": "BNS Section 95",
        "punishmentSection": "BNS Section 95",
        "punishment": "3 to 10 years imprisonment and fine; additional punishment may apply if the offence is committed",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class / Court by which underlying offence is triable",
        "evidence": ["Messages", "Payment records", "Witness statements", "CCTV"]
    },

    # 35
    {
        "id": 35,
        "case": "Procuration of child",
        "keywords": ["procuring child", "child exploitation", "force child", "child illicit intercourse"],
        "offenceSection": "BNS Section 96",
        "punishmentSection": "BNS Section 96",
        "punishment": "Imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Messages", "Witness statements", "Travel records", "Digital evidence"]
    },

    # 36
    {
        "id": 36,
        "case": "Kidnapping child under ten to steal property",
        "keywords": ["kidnap child", "child kidnapping theft", "steal from child", "kidnapping for theft"],
        "offenceSection": "BNS Section 97",
        "punishmentSection": "BNS Section 97",
        "punishment": "Imprisonment up to 7 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["CCTV", "Witness statements", "Phone location", "Stolen property records"]
    },

    # 37
    {
        "id": 37,
        "case": "Selling child for prostitution or unlawful purpose",
        "keywords": ["sell child", "child prostitution", "child trafficking", "child exploitation"],
        "offenceSection": "BNS Section 98",
        "punishmentSection": "BNS Section 98",
        "punishment": "Imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Messages", "Financial records", "Witness statements", "Digital evidence"]
    },

    # 38
    {
        "id": 38,
        "case": "Buying child for prostitution or unlawful purpose",
        "keywords": ["buy child", "child prostitution", "child exploitation", "illegal child purchase"],
        "offenceSection": "BNS Section 99",
        "punishmentSection": "BNS Section 99",
        "punishment": "7 to 14 years imprisonment and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Payment records", "Messages", "Witness statements", "Digital evidence"]
    },

    # 39
    {
        "id": 39,
        "case": "Organised crime",
        "keywords": ["organised crime", "organized crime", "crime syndicate", "gang crime"],
        "offenceSection": "BNS Section 111",
        "punishmentSection": "BNS Section 111",
        "punishment": "Punishment depends on the subsection; serious cases can attract life imprisonment or death and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Financial records", "Communication records", "Digital evidence", "Witness statements"]
    },

    # 40
    {
        "id": 40,
        "case": "Petty organised crime",
        "keywords": ["petty organised crime", "gang theft", "gang cheating", "shoplifting gang", "pickpocket gang"],
        "offenceSection": "BNS Section 112",
        "punishmentSection": "BNS Section 112",
        "punishment": "1 to 7 years imprisonment and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["CCTV", "Gang communication", "Witness statements", "Transaction records"]
    },

    # 41
    {
        "id": 41,
        "case": "Terrorist act",
        "keywords": ["terrorist act", "terrorism", "terror attack", "terrorist activity"],
        "offenceSection": "BNS Section 113",
        "punishmentSection": "BNS Section 113",
        "punishment": "Punishment varies by subsection and circumstances; may include imprisonment for life or other severe punishment",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Digital evidence", "Financial records", "Forensic evidence", "Communication records"]
    },

    # 42
    {
        "id": 42,
        "case": "Voluntarily causing hurt",
        "keywords": ["hurt", "beat person", "injury", "physical assault", "causing hurt"],
        "offenceSection": "BNS Section 115",
        "punishmentSection": "BNS Section 115",
        "punishment": "Up to 1 year imprisonment, or fine up to Rs. 10,000, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Medical report", "Witness statements", "CCTV", "Photographs"]
    },

    # 43
    {
        "id": 43,
        "case": "Voluntarily causing grievous hurt",
        "keywords": ["grievous hurt", "serious injury", "fracture", "permanent injury"],
        "offenceSection": "BNS Section 117",
        "punishmentSection": "BNS Section 117",
        "punishment": "Up to 7 years and fine; enhanced punishment applies in specified circumstances",
        "classification": "Cognizable, Bailable or Non-bailable depending on subsection",
        "court": "Any Magistrate or Court of Session depending on subsection",
        "evidence": ["Medical report", "X-ray", "Doctor evidence", "CCTV"]
    },

    # 44
    {
        "id": 44,
        "case": "Causing hurt by dangerous weapons",
        "keywords": ["knife attack", "weapon injury", "dangerous weapon", "stab injury"],
        "offenceSection": "BNS Section 118",
        "punishmentSection": "BNS Section 118",
        "punishment": "For hurt, up to 3 years/fine/both; grievous hurt has much higher punishment",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate / Magistrate of First Class depending on subsection",
        "evidence": ["Weapon", "Medical report", "Forensic evidence", "CCTV"]
    },

    # 45
    {
        "id": 45,
        "case": "Causing hurt to extort property",
        "keywords": ["hurt for money", "extort property", "physical torture for money", "extortion injury"],
        "offenceSection": "BNS Section 119",
        "punishmentSection": "BNS Section 119",
        "punishment": "Up to 10 years and fine; grievous hurt can attract life imprisonment or up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class / Court of Session",
        "evidence": ["Medical report", "Payment records", "Messages", "Witness statements"]
    },

    # 46
    {
        "id": 46,
        "case": "Causing hurt to extort confession",
        "keywords": ["torture confession", "force confession", "hurt for confession", "police torture"],
        "offenceSection": "BNS Section 120",
        "punishmentSection": "BNS Section 120",
        "punishment": "Up to 7 years and fine for hurt; up to 10 years and fine for grievous hurt",
        "classification": "Cognizable, Bailable or Non-bailable depending on subsection",
        "court": "Magistrate of First Class / Court of Session",
        "evidence": ["Medical report", "CCTV", "Witness statements", "Recording"]
    },

    # 47
    {
        "id": 47,
        "case": "Causing hurt to deter public servant",
        "keywords": ["attack police", "hurt public servant", "assault government officer", "deter public servant"],
        "offenceSection": "BNS Section 121",
        "punishmentSection": "BNS Section 121",
        "punishment": "Up to 5 years for hurt; higher punishment for grievous hurt",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of First Class / Court of Session",
        "evidence": ["Medical report", "Official duty records", "CCTV", "Witness statements"]
    },

    # 48
    {
        "id": 48,
        "case": "Causing hurt on grave and sudden provocation",
        "keywords": ["provocation", "sudden provocation", "fight after provocation", "hurt provocation"],
        "offenceSection": "BNS Section 122",
        "punishmentSection": "BNS Section 122",
        "punishment": "Up to 1 month or fine up to Rs. 5,000 or both; grievous hurt has higher punishment",
        "classification": "Depends on subsection",
        "court": "Any Magistrate / Magistrate of First Class",
        "evidence": ["Witness statements", "CCTV", "Medical report", "Messages"]
    },

    # 49
    {
        "id": 49,
        "case": "Causing hurt using poison or intoxicating substance",
        "keywords": ["poison", "poisoning", "drugging person", "intoxicating substance"],
        "offenceSection": "BNS Section 123",
        "punishmentSection": "BNS Section 123",
        "punishment": "Imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Toxicology report", "Medical report", "Container/sample", "Forensic evidence"]
    },

    # 50
    {
        "id": 50,
        "case": "Acid attack causing grievous hurt",
        "keywords": ["acid attack", "acid thrown", "acid injury", "acid violence"],
        "offenceSection": "BNS Section 124",
        "punishmentSection": "BNS Section 124",
        "punishment": "10 years to life imprisonment and fine; attempt to throw/administer acid has 5 to 7 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Medical report", "Acid/container evidence", "CCTV", "Forensic evidence"]
    },

    # 51
    {
        "id": 51,
        "case": "Act endangering life or personal safety",
        "keywords": ["endanger life", "dangerous act", "rash act", "negligent act"],
        "offenceSection": "BNS Section 125",
        "punishmentSection": "BNS Section 125",
        "punishment": "Up to 3 months; higher punishment where hurt or grievous hurt is caused",
        "classification": "Cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Witness statements", "Medical report", "Scene evidence"]
    },

    # 52
    {
        "id": 52,
        "case": "Assault or criminal force without grave provocation",
        "keywords": ["assault", "criminal force", "physical attack", "attack person"],
        "offenceSection": "BNS Section 131",
        "punishmentSection": "BNS Section 131",
        "punishment": "Up to 3 months imprisonment, or fine up to Rs. 1,000, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Witness statements", "Photographs", "Medical report"]
    },

    # 53
    {
        "id": 53,
        "case": "Assault on public servant",
        "keywords": ["attack police officer", "assault public servant", "attack officer", "criminal force officer"],
        "offenceSection": "BNS Section 132",
        "punishmentSection": "BNS Section 132",
        "punishment": "Imprisonment up to 2 years, or fine, or both",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Official records", "Witness statements", "Medical report"]
    },

    # 54
    {
        "id": 54,
        "case": "Assault with intent to dishonour",
        "keywords": ["dishonour assault", "insult by assault", "criminal force dishonour"],
        "offenceSection": "BNS Section 133",
        "punishmentSection": "BNS Section 133",
        "punishment": "Up to 2 years imprisonment, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Witness statements", "CCTV", "Messages", "Video recording"]
    },

    # 55
    {
        "id": 55,
        "case": "Assault while attempting theft",
        "keywords": ["assault for theft", "snatching attempt", "attack during theft", "theft assault"],
        "offenceSection": "BNS Section 134",
        "punishmentSection": "BNS Section 134",
        "punishment": "Up to 2 years imprisonment, or fine, or both",
        "classification": "Cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Stolen property", "Witness statements", "Fingerprints"]
    },

    # 56
    {
        "id": 56,
        "case": "Assault while attempting wrongful confinement",
        "keywords": ["assault confinement", "force to confine", "wrongful confinement attempt"],
        "offenceSection": "BNS Section 135",
        "punishmentSection": "BNS Section 135",
        "punishment": "Up to 1 year imprisonment, or fine up to Rs. 5,000, or both",
        "classification": "Cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Witness statements", "Messages", "Medical report"]
    },

    # 57
    {
        "id": 57,
        "case": "Assault on grave and sudden provocation",
        "keywords": ["assault provocation", "sudden provocation fight", "grave provocation"],
        "offenceSection": "BNS Section 136",
        "punishmentSection": "BNS Section 136",
        "punishment": "Up to 1 month simple imprisonment, or fine up to Rs. 1,000, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Witness statements", "CCTV", "Messages", "Video recording"]
    },

    # 58
    {
        "id": 58,
        "case": "Kidnapping",
        "keywords": ["kidnap", "kidnapping", "take child", "take person away"],
        "offenceSection": "BNS Section 137",
        "punishmentSection": "BNS Section 137(2)",
        "punishment": "Imprisonment up to 7 years and fine",
        "classification": "Cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["CCTV", "Phone location", "Witness statements", "Travel records"]
    },

    # 59
    {
        "id": 59,
        "case": "Kidnapping child for begging",
        "keywords": ["child begging", "kidnap for begging", "begging gang", "child begging gang"],
        "offenceSection": "BNS Section 139(1)",
        "punishmentSection": "BNS Section 139(1)",
        "punishment": "10 years to life imprisonment and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["CCTV", "Child protection records", "Witness statements", "Financial records"]
    },

    # 60
    {
        "id": 60,
        "case": "Kidnapping or abducting to murder",
        "keywords": ["kidnap murder", "kidnapping to kill", "abduction murder", "kidnap and kill"],
        "offenceSection": "BNS Section 140(1)",
        "punishmentSection": "BNS Section 140(1)",
        "punishment": "Life imprisonment, or rigorous imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["CCTV", "Phone records", "Witness statements", "Forensic evidence"]
    },

    # 61
    {
        "id": 61,
        "case": "Kidnapping for ransom",
        "keywords": ["ransom", "kidnap for money", "ransom demand", "kidnapping ransom"],
        "offenceSection": "BNS Section 140(2)",
        "punishmentSection": "BNS Section 140(2)",
        "punishment": "Death or life imprisonment and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Ransom messages", "Call records", "Bank records", "CCTV"]
    },

    # 62
    {
        "id": 62,
        "case": "Wrongfully concealing kidnapped or abducted person",
        "keywords": ["hide kidnapped person", "conceal kidnapped person", "abducted person hidden"],
        "offenceSection": "BNS Section 142",
        "punishmentSection": "BNS Section 142",
        "punishment": "Punishment corresponding to the kidnapping or abduction",
        "classification": "Cognizable, Non-bailable",
        "court": "Court by which kidnapping or abduction is triable",
        "evidence": ["Location records", "CCTV", "Witness statements", "Communication records"]
    },

    # 63
    {
        "id": 63,
        "case": "Human trafficking",
        "keywords": ["human trafficking", "people trafficking", "trafficking person", "forced exploitation"],
        "offenceSection": "BNS Section 143",
        "punishmentSection": "BNS Section 143",
        "punishment": "Generally 7 to 10 years and fine; higher punishment applies for trafficking multiple persons or children",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Travel records", "Financial records", "Messages", "Witness statements"]
    },

    # 64
    {
        "id": 64,
        "case": "Theft",
        "keywords": ["theft", "steal", "stolen", "stealing", "take property"],
        "offenceSection": "BNS Section 303",
        "punishmentSection": "BNS Section 303(2)",
        "punishment": "Up to 3 years imprisonment, or fine, or both; repeat conviction can attract 1 to 5 years and fine",
        "classification": "Cognizable, Non-bailable; special treatment may apply for first theft below Rs. 5,000",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Stolen property", "Witness statements", "Fingerprints"]
    },

    # 65
    {
        "id": 65,
        "case": "Snatching",
        "keywords": ["snatching", "phone snatching", "chain snatching", "bag snatching"],
        "offenceSection": "BNS Section 304",
        "punishmentSection": "BNS Section 304(2)",
        "punishment": "Imprisonment up to 3 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Stolen phone/property", "Witness statements", "Vehicle records"]
    },

    # 66
    {
        "id": 66,
        "case": "Theft in dwelling house or place of worship",
        "keywords": ["house theft", "home theft", "temple theft", "theft in house", "theft in place of worship"],
        "offenceSection": "BNS Section 305",
        "punishmentSection": "BNS Section 305",
        "punishment": "Imprisonment up to 7 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Fingerprints", "Broken locks", "Recovered property"]
    },

    # 67
    {
        "id": 67,
        "case": "Theft by clerk or servant",
        "keywords": ["employee theft", "servant theft", "clerk theft", "employee stole"],
        "offenceSection": "BNS Section 306",
        "punishmentSection": "BNS Section 306",
        "punishment": "Imprisonment up to 7 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": ["Employment records", "CCTV", "Inventory records", "Financial records"]
    },

    # 68
    {
        "id": 68,
        "case": "Theft after preparation to cause hurt or restraint",
        "keywords": ["armed theft", "theft with weapon", "theft prepared to hurt", "dangerous theft"],
        "offenceSection": "BNS Section 307",
        "punishmentSection": "BNS Section 307",
        "punishment": "Rigorous imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Weapon", "CCTV", "Stolen property", "Witness statements"]
    },

    # 69
    {
        "id": 69,
        "case": "Extortion",
        "keywords": ["extortion", "threat for money", "demand money threat", "blackmail money"],
        "offenceSection": "BNS Section 308",
        "punishmentSection": "BNS Section 308(2)",
        "punishment": "Imprisonment up to 7 years, or fine, or both",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Threat messages", "Call recordings", "Bank records", "Witness statements"]
    },

    # 70
    {
        "id": 70,
        "case": "Robbery",
        "keywords": ["robbery", "rob", "armed robbery", "force and theft"],
        "offenceSection": "BNS Section 309",
        "punishmentSection": "BNS Section 309(4)",
        "punishment": "Rigorous imprisonment up to 10 years and fine; highway robbery between sunset and sunrise can attract up to 14 years",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["CCTV", "Weapon", "Witness statements", "Recovered property"]
    },

    # 71
    {
        "id": 71,
        "case": "Dacoity",
        "keywords": ["dacoity", "gang robbery", "five persons robbery", "dacoit"],
        "offenceSection": "BNS Section 310",
        "punishmentSection": "BNS Section 310(2)",
        "punishment": "Life imprisonment, or rigorous imprisonment up to 10 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["CCTV", "Weapons", "Communication records", "Witness statements"]
    },

    # 72
    {
        "id": 72,
        "case": "Robbery or dacoity with attempt to cause death or grievous hurt",
        "keywords": ["robbery attack", "dacoity attack", "robbery with weapon", "robbery serious injury"],
        "offenceSection": "BNS Section 311",
        "punishmentSection": "BNS Section 311",
        "punishment": "Imprisonment of not less than 7 years",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Weapon", "Medical report", "CCTV", "Forensic evidence"]
    },

    # 73
    {
        "id": 73,
        "case": "Attempted robbery or dacoity while armed with deadly weapon",
        "keywords": ["armed robbery attempt", "deadly weapon robbery", "attempt dacoity weapon"],
        "offenceSection": "BNS Section 312",
        "punishmentSection": "BNS Section 312",
        "punishment": "Imprisonment of not less than 7 years",
        "classification": "Cognizable, Non-bailable",
        "court": "Court of Session",
        "evidence": ["Weapon", "CCTV", "Witness statements", "Forensic evidence"]
    },

    # 74
    {
        "id": 74,
        "case": "Dishonest misappropriation of property",
        "keywords": ["misappropriation", "wrongfully use property", "dishonest property use", "property misuse"],
        "offenceSection": "BNS Section 314",
        "punishmentSection": "BNS Section 314",
        "punishment": "6 months to 2 years imprisonment and fine",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Ownership records", "Transaction records", "Documents", "Witness statements"]
    },

    # 75
    {
        "id": 75,
        "case": "Misappropriation of property belonging to deceased person",
        "keywords": ["deceased property", "dead person's property", "inheritance property theft", "misappropriate deceased property"],
        "offenceSection": "BNS Section 315",
        "punishmentSection": "BNS Section 315",
        "punishment": "Up to 3 years and fine; higher punishment may apply to clerk or employee",
        "classification": "Non-cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Will", "Property records", "Bank records", "Witness statements"]
    },

    # 76
    {
        "id": 76,
        "case": "Criminal breach of trust",
        "keywords": ["breach of trust", "money entrusted", "property entrusted", "misuse entrusted property"],
        "offenceSection": "BNS Section 316",
        "punishmentSection": "BNS Section 316(2)",
        "punishment": "Up to 5 years imprisonment, or fine, or both",
        "classification": "Cognizable, Non-bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Agreement", "Bank records", "Receipts", "Communication records"]
    },

    # 77
    {
        "id": 77,
        "case": "Dishonestly receiving stolen property",
        "keywords": ["receive stolen property", "buy stolen goods", "stolen goods", "knowingly receive stolen"],
        "offenceSection": "BNS Section 317",
        "punishmentSection": "BNS Section 317(2)",
        "punishment": "Up to 3 years imprisonment, or fine, or both",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": ["Recovered property", "Purchase records", "Messages", "Witness statements"]
    },

    # 78
    {
        "id": 78,
        "case": "Cheating",
        "keywords": ["cheating", "fraud", "deceive", "deceived", "cheated"],
        "offenceSection": "BNS Section 318",
        "punishmentSection": "BNS Section 318(2)",
        "punishment": "Up to 3 years imprisonment, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Messages", "Agreements", "Bank records", "Transaction records"]
    },

    # 79
    {
        "id": 79,
        "case": "Cheating by personation",
        "keywords": ["fake identity", "personation", "pretend to be someone", "identity fraud"],
        "offenceSection": "BNS Section 319",
        "punishmentSection": "BNS Section 319(2)",
        "punishment": "Up to 5 years imprisonment, or fine, or both",
        "classification": "Cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Identity documents", "Digital records", "Messages", "Financial records"]
    },

    # 80
    {
        "id": 80,
        "case": "Criminal trespass",
        "keywords": ["trespass", "enter property", "illegal entry", "property trespass"],
        "offenceSection": "BNS Section 329",
        "punishmentSection": "BNS Section 329(3)",
        "punishment": "Imprisonment up to 3 months, or fine up to Rs. 5,000, or both",
        "classification": "Cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["CCTV", "Property documents", "Witness statements", "Photographs"]
    },

    # 81
    {
        "id": 81,
        "case": "Lurking house-trespass or house-breaking",
        "keywords": ["house breaking", "break into house", "night trespass", "burglary"],
        "offenceSection": "BNS Section 331",
        "punishmentSection": "BNS Section 331",
        "punishment": "Punishment varies by circumstances; can range from 2 years to severe imprisonment",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate / Magistrate of First Class / Court of Session depending on subsection",
        "evidence": ["Broken lock", "CCTV", "Fingerprints", "Recovered property"]
    },

    # 82
    {
        "id": 82,
        "case": "House-trespass to commit serious offence",
        "keywords": ["house trespass crime", "enter house to commit offence", "burglary", "illegal house entry"],
        "offenceSection": "BNS Section 332",
        "punishmentSection": "BNS Section 332",
        "punishment": "Punishment depends on the offence intended; can include life imprisonment or imprisonment up to 10 years",
        "classification": "Cognizable, Non-bailable or Bailable depending on subsection",
        "court": "Court of Session or Any Magistrate depending on subsection",
        "evidence": ["CCTV", "Broken doors", "Tools", "Forensic evidence"]
    },

    # 83
    {
        "id": 83,
        "case": "House-trespass after preparation to cause hurt",
        "keywords": ["house trespass weapon", "break into house with weapon", "house breaking attack"],
        "offenceSection": "BNS Section 333",
        "punishmentSection": "BNS Section 333",
        "punishment": "Imprisonment up to 7 years and fine",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": ["Weapon", "CCTV", "Broken locks", "Witness statements"]
    },

    # 84
    {
        "id": 84,
        "case": "Breaking open a closed receptacle containing property",
        "keywords": ["break locker", "break box", "open locked container", "closed receptacle"],
        "offenceSection": "BNS Section 334",
        "punishmentSection": "BNS Section 334(1)",
        "punishment": "Up to 2 years imprisonment, or fine, or both",
        "classification": "Cognizable, Non-bailable",
        "court": "Any Magistrate",
        "evidence": ["Container", "Broken lock", "CCTV", "Fingerprints"]
    },

    # 85
    {
        "id": 85,
        "case": "Criminal intimidation",
        "keywords": ["criminal intimidation", "threat", "threaten person", "death threat", "threat message"],
        "offenceSection": "BNS Section 351",
        "punishmentSection": "BNS Section 351(2)",
        "punishment": "Up to 2 years imprisonment, or fine, or both; serious threats can attract higher punishment",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate / Magistrate of First Class depending on subsection",
        "evidence": ["Threat messages", "Call recordings", "Witness statements", "Social media records"]
    },

    # 86
    {
        "id": 86,
        "case": "Intentional insult provoking breach of peace",
        "keywords": ["intentional insult", "provoking fight", "insult", "breach of peace"],
        "offenceSection": "BNS Section 352",
        "punishmentSection": "BNS Section 352",
        "punishment": "Up to 2 years imprisonment, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Witness statements", "Audio recording", "Video", "Messages"]
    },

    # 87
    {
        "id": 87,
        "case": "Statements causing public mischief",
        "keywords": ["false rumour", "false information", "public mischief", "rumour", "hate message"],
        "offenceSection": "BNS Section 353",
        "punishmentSection": "BNS Section 353",
        "punishment": "Generally up to 3 years, fine, or both; higher punishment may apply in specified circumstances",
        "classification": "Depends on subsection",
        "court": "Any Magistrate / Magistrate of First Class depending on subsection",
        "evidence": ["Social media post", "Messages", "Digital forensic report", "Screenshots"]
    },

    # 88
    {
        "id": 88,
        "case": "Inducing person to believe in divine displeasure",
        "keywords": ["divine displeasure", "religious threat", "threat by superstition", "fear of divine punishment"],
        "offenceSection": "BNS Section 354",
        "punishmentSection": "BNS Section 354",
        "punishment": "Imprisonment up to 1 year, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Messages", "Audio recording", "Witness statements", "Video"]
    },

    # 89
    {
        "id": 89,
        "case": "Misconduct in public by a drunken person",
        "keywords": ["drunk in public", "drunken behaviour", "public intoxication", "drunk person"],
        "offenceSection": "BNS Section 355",
        "punishmentSection": "BNS Section 355",
        "punishment": "Simple imprisonment up to 24 hours, fine up to Rs. 1,000, or both, or community service",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Witness statements", "Police report", "CCTV", "Medical/breath evidence"]
    },

    # 90
    {
        "id": 90,
        "case": "Defamation",
        "keywords": ["defamation", "defame", "reputation damage", "false accusation", "defamatory statement"],
        "offenceSection": "BNS Section 356",
        "punishmentSection": "BNS Section 356(2)",
        "punishment": "Up to 2 years simple imprisonment, or fine, or both, or community service",
        "classification": "Non-cognizable, Bailable",
        "court": "Magistrate of the First Class; special public-function cases may be before Court of Session",
        "evidence": ["Published statement", "Social media post", "Messages", "Witness statements"]
    },

    # 91
    {
        "id": 91,
        "case": "Breach of contract to attend helpless person",
        "keywords": ["neglect helpless person", "abandon helpless person", "care contract", "failure to provide care"],
        "offenceSection": "BNS Section 357",
        "punishmentSection": "BNS Section 357",
        "punishment": "Imprisonment up to 3 months, or fine up to Rs. 5,000, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Contract", "Care records", "Witness statements", "Medical records"]
    },

    # 92
    {
        "id": 92,
        "case": "Dishonestly making false claim in Court",
        "keywords": ["false court claim", "fake claim court", "false claim", "dishonest court claim"],
        "offenceSection": "BNS Section 246",
        "punishmentSection": "BNS Section 246",
        "punishment": "Imprisonment up to 2 years and fine",
        "classification": "Non-cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Court documents", "False claim records", "Supporting documents", "Witness statements"]
    },

    # 93
    {
        "id": 93,
        "case": "Fraudulently obtaining decree for amount not due",
        "keywords": ["fake decree", "fraud court decree", "amount not due", "fraudulent court order"],
        "offenceSection": "BNS Section 247",
        "punishmentSection": "BNS Section 247",
        "punishment": "Up to 2 years imprisonment, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Court records", "Financial documents", "Decree", "Transaction records"]
    },

    # 94
    {
        "id": 94,
        "case": "False charge of offence made with intent to injure",
        "keywords": ["false criminal case", "false charge", "fake complaint", "false accusation"],
        "offenceSection": "BNS Section 248",
        "punishmentSection": "BNS Section 248(a)/(b)",
        "punishment": "Up to 5 years or fine or both in ordinary cases; up to 10 years and fine for specified serious false charges",
        "classification": "Non-cognizable, Bailable",
        "court": "Magistrate of the First Class / Court of Session depending on subsection",
        "evidence": ["Complaint records", "Court records", "Messages", "Witness statements"]
    },

    # 95
    {
        "id": 95,
        "case": "Harbouring an offender",
        "keywords": ["hide criminal", "harbour offender", "hide accused", "help offender escape"],
        "offenceSection": "BNS Section 249",
        "punishmentSection": "BNS Section 249",
        "punishment": "Punishment depends on the offence being concealed; serious cases can attract up to 5 years or other specified punishment",
        "classification": "Cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Location records", "CCTV", "Communication records", "Witness statements"]
    },

    # 96
    {
        "id": 96,
        "case": "Giving false information about an offence",
        "keywords": ["false information police", "false crime information", "fake information about crime", "false report"],
        "offenceSection": "BNS Section 240",
        "punishmentSection": "BNS Section 240",
        "punishment": "Imprisonment up to 2 years, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Complaint records", "Messages", "Call records", "Witness statements"]
    },

    # 97
    {
        "id": 97,
        "case": "Destroying document or electronic record to prevent evidence",
        "keywords": ["destroy evidence", "delete evidence", "destroy document", "delete electronic record"],
        "offenceSection": "BNS Section 241",
        "punishmentSection": "BNS Section 241",
        "punishment": "Imprisonment up to 3 years, or fine up to Rs. 5,000, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Deleted files", "Device forensic report", "Document history", "Backup records"]
    },

    # 98
    {
        "id": 98,
        "case": "False personation in a suit or prosecution",
        "keywords": ["false personation court", "fake identity court", "pretend to be accused", "false personation prosecution"],
        "offenceSection": "BNS Section 242",
        "punishmentSection": "BNS Section 242",
        "punishment": "Imprisonment up to 3 years, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Magistrate of the First Class",
        "evidence": ["Court records", "Identity documents", "CCTV", "Witness statements"]
    },

    # 99
    {
        "id": 99,
        "case": "Fraudulent removal or concealment of property",
        "keywords": ["hide property", "remove property illegally", "hide assets", "prevent property seizure"],
        "offenceSection": "BNS Section 243",
        "punishmentSection": "BNS Section 243",
        "punishment": "Imprisonment up to 3 years, or fine up to Rs. 5,000, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Property records", "Transfer documents", "Bank records", "Transaction history"]
    },

    # 100
    {
        "id": 100,
        "case": "Fraudulent claim to property to prevent seizure",
        "keywords": ["false property claim", "fake property claim", "fraudulent property claim", "hide property seizure"],
        "offenceSection": "BNS Section 244",
        "punishmentSection": "BNS Section 244",
        "punishment": "Imprisonment up to 2 years, or fine, or both",
        "classification": "Non-cognizable, Bailable",
        "court": "Any Magistrate",
        "evidence": ["Property documents", "Court records", "Ownership records", "Transaction records"]
    }
    ,# 101
    {
        "id": 101,
        "case": "Fraudulently suffering decree for sum not due",
        "keywords": ["fraudulent decree", "false decree", "sum not due", "fake court decree"],
        "offenceSection": "BNS Section 245",
        "punishmentSection": "BNS Section 245",
        "punishment": "Up to 2 years imprisonment, or fine, or both",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Court records", "Financial documents", "Decree", "Transaction records"]
    },

    # 102
    {
        "id": 102,
        "case": "Dishonestly making false claim in Court",
        "keywords": ["false court claim", "fake claim", "false claim in court", "dishonest claim"],
        "offenceSection": "BNS Section 246",
        "punishmentSection": "BNS Section 246",
        "punishment": "Up to 2 years imprisonment and fine",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Court documents", "False records", "Witness statements"]
    },

    # 103
    {
        "id": 103,
        "case": "Fraudulently obtaining decree for sum not due",
        "keywords": ["fraudulent decree", "obtain fake decree", "wrong amount decree"],
        "offenceSection": "BNS Section 247",
        "punishmentSection": "BNS Section 247",
        "punishment": "Up to 2 years imprisonment, or fine, or both",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Court records", "Financial records", "Documents"]
    },

    # 104
    {
        "id": 104,
        "case": "False charge of offence made with intent to injure",
        "keywords": ["false charge", "false criminal case", "fake accusation", "false complaint"],
        "offenceSection": "BNS Section 248",
        "punishmentSection": "BNS Section 248",
        "punishment": "Up to 5 years or fine or both; serious false charges have higher punishment",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Complaint records", "Court records", "Messages", "Witness statements"]
    },

    # 105
    {
        "id": 105,
        "case": "Harbouring offender",
        "keywords": ["hide offender", "harbour criminal", "help criminal hide", "hide accused"],
        "offenceSection": "BNS Section 249",
        "punishmentSection": "BNS Section 249",
        "punishment": "Punishment depends on the offence of the offender being harboured",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Location records", "Communication records"]
    },

    # 106
    {
        "id": 106,
        "case": "Taking gift to screen offender",
        "keywords": ["money to hide criminal", "gift to screen offender", "bribe to hide offender"],
        "offenceSection": "BNS Section 250",
        "punishmentSection": "BNS Section 250",
        "punishment": "Punishment as provided by the section depending on the underlying offence",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Payment records", "Messages", "Bank records", "Witness statements"]
    },

    # 107
    {
        "id": 107,
        "case": "Offering gift to screen offender",
        "keywords": ["offer money to hide criminal", "gift to hide offender", "screen offender"],
        "offenceSection": "BNS Section 251",
        "punishmentSection": "BNS Section 251",
        "punishment": "Punishment as provided by the section depending on the underlying offence",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Messages", "Bank records", "Payment records"]
    },

    # 108
    {
        "id": 108,
        "case": "Taking gift to help recover stolen property",
        "keywords": ["money to recover stolen property", "gift for stolen property", "recover stolen goods"],
        "offenceSection": "BNS Section 252",
        "punishmentSection": "BNS Section 252",
        "punishment": "Imprisonment and/or fine as provided by BNS Section 252",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Payment records", "Messages", "Stolen property records"]
    },

    # 109
    {
        "id": 109,
        "case": "Harbouring offender who escaped from custody",
        "keywords": ["hide escaped prisoner", "help escaped offender", "escaped criminal"],
        "offenceSection": "BNS Section 253",
        "punishmentSection": "BNS Section 253",
        "punishment": "Punishment as provided by BNS Section 253",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Location records", "Communication records"]
    },

    # 110
    {
        "id": 110,
        "case": "Harbouring robbers or dacoits",
        "keywords": ["hide robber", "hide dacoit", "harbour robber", "help dacoit"],
        "offenceSection": "BNS Section 254",
        "punishmentSection": "BNS Section 254",
        "punishment": "Imprisonment and fine as provided by BNS Section 254",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Communication records", "Witness statements"]
    },

    # 111
    {
        "id": 111,
        "case": "Public servant disobeying law to save person from punishment",
        "keywords": ["public servant save offender", "official disobey law", "protect criminal"],
        "offenceSection": "BNS Section 255",
        "punishmentSection": "BNS Section 255",
        "punishment": "Punishment as provided by BNS Section 255",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Official records", "Orders", "Communication records"]
    },

    # 112
    {
        "id": 112,
        "case": "Public servant framing incorrect record",
        "keywords": ["false official record", "public servant false record", "incorrect record"],
        "offenceSection": "BNS Section 256",
        "punishmentSection": "BNS Section 256",
        "punishment": "Punishment as provided by BNS Section 256",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Official records", "Documents", "Digital records"]
    },

    # 113
    {
        "id": 113,
        "case": "Public servant corruptly making report contrary to law",
        "keywords": ["false official report", "corrupt public servant", "illegal report"],
        "offenceSection": "BNS Section 257",
        "punishmentSection": "BNS Section 257",
        "punishment": "Punishment as provided by BNS Section 257",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Official report", "Government records", "Communication records"]
    },

    # 114
    {
        "id": 114,
        "case": "Illegal commitment for trial or confinement",
        "keywords": ["illegal detention", "illegal confinement", "wrongful commitment"],
        "offenceSection": "BNS Section 258",
        "punishmentSection": "BNS Section 258",
        "punishment": "Punishment as provided by BNS Section 258",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Custody records", "Court orders", "Official records"]
    },

    # 115
    {
        "id": 115,
        "case": "Public servant intentionally failing to apprehend offender",
        "keywords": ["police fail arrest", "public servant failure arrest", "not arrest offender"],
        "offenceSection": "BNS Section 259",
        "punishmentSection": "BNS Section 259",
        "punishment": "Punishment as provided by BNS Section 259",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Arrest records", "Police records", "Orders"]
    },

    # 116
    {
        "id": 116,
        "case": "Public servant intentionally allowing sentenced person to escape",
        "keywords": ["help prisoner escape", "police allow escape", "prison escape assistance"],
        "offenceSection": "BNS Section 260",
        "punishmentSection": "BNS Section 260",
        "punishment": "Punishment as provided by BNS Section 260",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Prison records", "CCTV", "Official records"]
    },

    # 117
    {
        "id": 117,
        "case": "Escape from confinement negligently suffered by public servant",
        "keywords": ["prisoner escaped", "negligent prison officer", "custody escape"],
        "offenceSection": "BNS Section 261",
        "punishmentSection": "BNS Section 261",
        "punishment": "Punishment as provided by BNS Section 261",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Prison records", "Duty records"]
    },

    # 118
    {
        "id": 118,
        "case": "Resistance to lawful apprehension",
        "keywords": ["resist arrest", "resistance arrest", "obstruct police arrest"],
        "offenceSection": "BNS Section 262",
        "punishmentSection": "BNS Section 262",
        "punishment": "Punishment as provided by BNS Section 262",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Police records", "Witness statements"]
    },

    # 119
    {
        "id": 119,
        "case": "Obstructing lawful apprehension of another person",
        "keywords": ["help person escape arrest", "obstruct arrest", "prevent arrest"],
        "offenceSection": "BNS Section 263",
        "punishmentSection": "BNS Section 263",
        "punishment": "Punishment as provided by BNS Section 263",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Witness statements", "Police records"]
    },

    # 120
    {
        "id": 120,
        "case": "Public servant omission to apprehend offender",
        "keywords": ["police did not arrest", "failure to apprehend", "public servant omission"],
        "offenceSection": "BNS Section 264",
        "punishmentSection": "BNS Section 264",
        "punishment": "Punishment as provided by BNS Section 264",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Police records", "Orders", "Official documents"]
    },

    # 121
    {
        "id": 121,
        "case": "Resistance or obstruction to lawful apprehension",
        "keywords": ["resist police", "escape arrest", "obstruct lawful arrest"],
        "offenceSection": "BNS Section 265",
        "punishmentSection": "BNS Section 265",
        "punishment": "Punishment as provided by BNS Section 265",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Police records", "Witness statements"]
    },

    # 122
    {
        "id": 122,
        "case": "Violation of condition of remission of punishment",
        "keywords": ["violate remission", "remission condition", "sentence remission violation"],
        "offenceSection": "BNS Section 266",
        "punishmentSection": "BNS Section 266",
        "punishment": "Punishment as provided by BNS Section 266",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Prison records", "Remission order", "Official records"]
    },

    # 123
    {
        "id": 123,
        "case": "Intentional insult to public servant in judicial proceeding",
        "keywords": ["insult judge", "insult public servant court", "interrupt court"],
        "offenceSection": "BNS Section 267",
        "punishmentSection": "BNS Section 267",
        "punishment": "Punishment as provided by BNS Section 267",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Court record", "Audio/video recording", "Witness statements"]
    },

    # 124
    {
        "id": 124,
        "case": "Personation of assessor",
        "keywords": ["fake assessor", "assessor personation", "pretend assessor"],
        "offenceSection": "BNS Section 268",
        "punishmentSection": "BNS Section 268",
        "punishment": "Punishment as provided by BNS Section 268",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Court records", "Identity documents", "Witness statements"]
    },

    # 125
    {
        "id": 125,
        "case": "Failure to appear in Court after release on bail bond",
        "keywords": ["bail violation", "fail to appear court", "not attend court", "bail bond"],
        "offenceSection": "BNS Section 269",
        "punishmentSection": "BNS Section 269",
        "punishment": "Punishment as provided by BNS Section 269",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Bail bond", "Court attendance records", "Court order"]
    },

    # 126
    {
        "id": 126,
        "case": "Public nuisance",
        "keywords": ["public nuisance", "nuisance", "public disturbance", "obstruction public"],
        "offenceSection": "BNS Section 270",
        "punishmentSection": "BNS Section 270",
        "punishment": "Punishment as provided by BNS Section 270",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Photographs", "Witness statements"]
    },

    # 127
    {
        "id": 127,
        "case": "Negligent act likely to spread dangerous infection",
        "keywords": ["spread infection", "negligent infection", "dangerous disease spread"],
        "offenceSection": "BNS Section 271",
        "punishmentSection": "BNS Section 271",
        "punishment": "Punishment as provided by BNS Section 271",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Medical records", "Laboratory reports", "Public health records"]
    },

    # 128
    {
        "id": 128,
        "case": "Malignant act likely to spread dangerous infection",
        "keywords": ["deliberately spread disease", "infection spread", "malignant infection act"],
        "offenceSection": "BNS Section 272",
        "punishmentSection": "BNS Section 272",
        "punishment": "Punishment as provided by BNS Section 272",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Medical records", "Laboratory reports", "Communication records"]
    },

    # 129
    {
        "id": 129,
        "case": "Disobedience to quarantine rule",
        "keywords": ["break quarantine", "quarantine violation", "ignore quarantine"],
        "offenceSection": "BNS Section 273",
        "punishmentSection": "BNS Section 273",
        "punishment": "Punishment as provided by BNS Section 273",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Quarantine order", "Government records", "CCTV"]
    },

    # 130
    {
        "id": 130,
        "case": "Adulteration of food or drink",
        "keywords": ["food adulteration", "adulterated food", "fake food", "food contamination"],
        "offenceSection": "BNS Section 274",
        "punishmentSection": "BNS Section 274",
        "punishment": "Punishment as provided by BNS Section 274",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Food sample", "Laboratory report", "Purchase records"]
    },

    # 131
    {
        "id": 131,
        "case": "Sale of noxious food or drink",
        "keywords": ["sell harmful food", "poisonous food", "noxious drink", "unsafe food"],
        "offenceSection": "BNS Section 275",
        "punishmentSection": "BNS Section 275",
        "punishment": "Punishment as provided by BNS Section 275",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Food sample", "Lab report", "Purchase receipt"]
    },

    # 132
    {
        "id": 132,
        "case": "Adulteration of drugs",
        "keywords": ["drug adulteration", "fake medicine", "adulterated medicine", "medicine contamination"],
        "offenceSection": "BNS Section 276",
        "punishmentSection": "BNS Section 276",
        "punishment": "Punishment as provided by BNS Section 276",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Drug sample", "Laboratory report", "Purchase records"]
    },

    # 133
    {
        "id": 133,
        "case": "Sale of adulterated drugs",
        "keywords": ["sell fake medicine", "sell adulterated drugs", "fake medicine sale"],
        "offenceSection": "BNS Section 277",
        "punishmentSection": "BNS Section 277",
        "punishment": "Punishment as provided by BNS Section 277",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Medicine sample", "Lab report", "Shop records"]
    },

    # 134
    {
        "id": 134,
        "case": "Selling drug as a different drug",
        "keywords": ["wrong medicine", "fake drug identity", "sell drug as another drug"],
        "offenceSection": "BNS Section 278",
        "punishmentSection": "BNS Section 278",
        "punishment": "Punishment as provided by BNS Section 278",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Drug packaging", "Laboratory report", "Purchase records"]
    },

    # 135
    {
        "id": 135,
        "case": "Fouling water of public spring or reservoir",
        "keywords": ["pollute water", "contaminate reservoir", "pollute public water"],
        "offenceSection": "BNS Section 279",
        "punishmentSection": "BNS Section 279",
        "punishment": "Punishment as provided by BNS Section 279",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Water sample", "Laboratory report", "Photographs"]
    },

    # 136
    {
        "id": 136,
        "case": "Making atmosphere noxious to health",
        "keywords": ["air pollution", "noxious atmosphere", "harmful air", "polluting air"],
        "offenceSection": "BNS Section 280",
        "punishmentSection": "BNS Section 280",
        "punishment": "Punishment as provided by BNS Section 280",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Pollution report", "Photographs", "Inspection report"]
    },

    # 137
    {
        "id": 137,
        "case": "Rash driving or riding on public way",
        "keywords": ["rash driving", "dangerous driving", "rash riding", "reckless driving"],
        "offenceSection": "BNS Section 281",
        "punishmentSection": "BNS Section 281",
        "punishment": "Punishment as provided by BNS Section 281",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Dashcam", "Witness statements", "Traffic records"]
    },

    # 138
    {
        "id": 138,
        "case": "Rash navigation of vessel",
        "keywords": ["rash boat driving", "dangerous navigation", "reckless vessel"],
        "offenceSection": "BNS Section 282",
        "punishmentSection": "BNS Section 282",
        "punishment": "Punishment as provided by BNS Section 282",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Navigation records", "CCTV", "Witness statements"]
    },

    # 139
    {
        "id": 139,
        "case": "Exhibition of false light, mark or buoy",
        "keywords": ["false navigation light", "false buoy", "false mark", "navigation danger"],
        "offenceSection": "BNS Section 283",
        "punishmentSection": "BNS Section 283",
        "punishment": "Punishment as provided by BNS Section 283",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Navigation records", "Photographs", "Witness statements"]
    },

    # 140
    {
        "id": 140,
        "case": "Conveying person by water in unsafe vessel",
        "keywords": ["unsafe boat", "overloaded boat", "unsafe vessel", "overloaded vessel"],
        "offenceSection": "BNS Section 284",
        "punishmentSection": "BNS Section 284",
        "punishment": "Punishment as provided by BNS Section 284",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Vessel records", "Passenger records", "Inspection report"]
    },

    # 141
    {
        "id": 141,
        "case": "Danger or obstruction in public way",
        "keywords": ["road obstruction", "public road obstruction", "danger public way", "block road"],
        "offenceSection": "BNS Section 285",
        "punishmentSection": "BNS Section 285",
        "punishment": "Punishment as provided by BNS Section 285",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Photographs", "CCTV", "Traffic records"]
    },

    # 142
    {
        "id": 142,
        "case": "Negligent conduct with poisonous substance",
        "keywords": ["poison negligence", "dangerous chemical negligence", "poisonous substance"],
        "offenceSection": "BNS Section 286",
        "punishmentSection": "BNS Section 286",
        "punishment": "Punishment as provided by BNS Section 286",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Chemical sample", "Safety records", "Inspection report"]
    },

    # 143
    {
        "id": 143,
        "case": "Negligent conduct with fire or combustible matter",
        "keywords": ["fire negligence", "combustible material", "unsafe fire", "fire hazard"],
        "offenceSection": "BNS Section 287",
        "punishmentSection": "BNS Section 287",
        "punishment": "Punishment as provided by BNS Section 287",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Fire report", "CCTV", "Inspection report"]
    },

    # 144
    {
        "id": 144,
        "case": "Negligent conduct with explosive substance",
        "keywords": ["explosive negligence", "unsafe explosives", "explosive substance"],
        "offenceSection": "BNS Section 288",
        "punishmentSection": "BNS Section 288",
        "punishment": "Punishment as provided by BNS Section 288",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Forensic report", "Explosive material", "Inspection records"]
    },

    # 145
    {
        "id": 145,
        "case": "Negligent conduct with machinery",
        "keywords": ["machinery negligence", "unsafe machine", "machine accident"],
        "offenceSection": "BNS Section 289",
        "punishmentSection": "BNS Section 289",
        "punishment": "Punishment as provided by BNS Section 289",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Machine inspection", "Safety records", "CCTV"]
    },

    # 146
    {
        "id": 146,
        "case": "Negligent conduct while pulling down or constructing buildings",
        "keywords": ["building collapse", "construction negligence", "unsafe building", "demolition negligence"],
        "offenceSection": "BNS Section 290",
        "punishmentSection": "BNS Section 290",
        "punishment": "Punishment as provided by BNS Section 290",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Construction records", "Engineer report", "CCTV"]
    },

    # 147
    {
        "id": 147,
        "case": "Negligent conduct with animal",
        "keywords": ["dangerous animal negligence", "animal attack", "negligent animal handling"],
        "offenceSection": "BNS Section 291",
        "punishmentSection": "BNS Section 291",
        "punishment": "Punishment as provided by BNS Section 291",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Animal records", "Medical report", "Witness statements"]
    },

    # 148
    {
        "id": 148,
        "case": "Punishment for public nuisance",
        "keywords": ["public nuisance punishment", "continue nuisance", "public disturbance"],
        "offenceSection": "BNS Section 292",
        "punishmentSection": "BNS Section 292",
        "punishment": "Punishment as provided by BNS Section 292",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Inspection report", "CCTV", "Witness statements"]
    },

    # 149
    {
        "id": 149,
        "case": "Continuance of nuisance after injunction",
        "keywords": ["continue nuisance", "court injunction nuisance", "ignore nuisance order"],
        "offenceSection": "BNS Section 293",
        "punishmentSection": "BNS Section 293",
        "punishment": "Punishment as provided by BNS Section 293",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Court order", "Inspection report", "Photographs"]
    },

    # 150
    {
        "id": 150,
        "case": "Sale of obscene books or material",
        "keywords": ["obscene books", "sell obscene material", "obscene publication"],
        "offenceSection": "BNS Section 294",
        "punishmentSection": "BNS Section 294",
        "punishment": "Punishment as provided by BNS Section 294",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Books", "Digital files", "Sales records"]
    },

    # 151
    {
        "id": 151,
        "case": "Sale of obscene objects to child",
        "keywords": ["obscene material child", "sell obscene object child", "child obscene material"],
        "offenceSection": "BNS Section 295",
        "punishmentSection": "BNS Section 295",
        "punishment": "Punishment as provided by BNS Section 295",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Digital evidence", "Sales records", "Messages"]
    },

    # 152
    {
        "id": 152,
        "case": "Obscene acts and songs",
        "keywords": ["obscene act", "obscene song", "public obscene behaviour"],
        "offenceSection": "BNS Section 296",
        "punishmentSection": "BNS Section 296",
        "punishment": "Punishment as provided by BNS Section 296",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Video", "Audio", "Witness statements"]
    },

    # 153
    {
        "id": 153,
        "case": "Keeping lottery office",
        "keywords": ["lottery office", "illegal lottery", "lottery business"],
        "offenceSection": "BNS Section 297",
        "punishmentSection": "BNS Section 297",
        "punishment": "Punishment as provided by BNS Section 297",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Lottery records", "Money records", "Digital records"]
    },

    # 154
    {
        "id": 154,
        "case": "Defiling place of worship",
        "keywords": ["defile temple", "damage mosque", "damage church", "place of worship insult"],
        "offenceSection": "BNS Section 298",
        "punishmentSection": "BNS Section 298",
        "punishment": "Punishment as provided by BNS Section 298",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Photographs", "Witness statements"]
    },

    # 155
    {
        "id": 155,
        "case": "Deliberate and malicious acts intended to outrage religious feelings",
        "keywords": ["religious insult", "religious feelings", "malicious religious act"],
        "offenceSection": "BNS Section 299",
        "punishmentSection": "BNS Section 299",
        "punishment": "Punishment as provided by BNS Section 299",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Social media posts", "Messages", "Video", "Witness statements"]
    },

    # 156
    {
        "id": 156,
        "case": "Disturbing religious assembly",
        "keywords": ["disturb prayer", "religious assembly disturbance", "interrupt religious meeting"],
        "offenceSection": "BNS Section 300",
        "punishmentSection": "BNS Section 300",
        "punishment": "Punishment as provided by BNS Section 300",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Video", "Witness statements"]
    },

    # 157
    {
        "id": 157,
        "case": "Trespassing on burial places",
        "keywords": ["burial place trespass", "graveyard trespass", "cemetery disturbance"],
        "offenceSection": "BNS Section 301",
        "punishmentSection": "BNS Section 301",
        "punishment": "Punishment as provided by BNS Section 301",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Photographs", "Witness statements"]
    },

    # 158
    {
        "id": 158,
        "case": "Words intended to wound religious feelings",
        "keywords": ["religious insult words", "wound religious feelings", "religious insult"],
        "offenceSection": "BNS Section 302",
        "punishmentSection": "BNS Section 302",
        "punishment": "Punishment as provided by BNS Section 302",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Audio", "Messages", "Social media", "Witness statements"]
    },

    # 159
    {
        "id": 159,
        "case": "Theft",
        "keywords": ["steal", "stolen", "theft", "stealing property"],
        "offenceSection": "BNS Section 303",
        "punishmentSection": "BNS Section 303",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Stolen property", "Fingerprints", "Witness statements"]
    },

    # 160
    {
        "id": 160,
        "case": "Snatching",
        "keywords": ["snatching", "phone snatching", "chain snatching", "bag snatching"],
        "offenceSection": "BNS Section 304",
        "punishmentSection": "BNS Section 304",
        "punishment": "Punishment as provided by BNS Section 304",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Stolen phone", "Vehicle records", "Witness statements"]
    },

    # 161
    {
        "id": 161,
        "case": "Theft in dwelling house or place of worship",
        "keywords": ["house theft", "temple theft", "home theft", "theft place worship"],
        "offenceSection": "BNS Section 305",
        "punishmentSection": "BNS Section 305",
        "punishment": "Punishment as provided by BNS Section 305",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Broken lock", "Fingerprints", "Recovered property"]
    },

    # 162
    {
        "id": 162,
        "case": "Theft by clerk or servant",
        "keywords": ["employee theft", "servant theft", "clerk stole", "employee stole"],
        "offenceSection": "BNS Section 306",
        "punishmentSection": "BNS Section 306",
        "punishment": "Punishment as provided by BNS Section 306",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Employment records", "CCTV", "Inventory records", "Financial records"]
    },

    # 163
    {
        "id": 163,
        "case": "Theft after preparation to cause hurt",
        "keywords": ["armed theft", "theft with weapon", "theft preparation hurt"],
        "offenceSection": "BNS Section 307",
        "punishmentSection": "BNS Section 307",
        "punishment": "Punishment as provided by BNS Section 307",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Weapon", "CCTV", "Stolen property", "Witness statements"]
    },

    # 164
    {
        "id": 164,
        "case": "Extortion",
        "keywords": ["extortion", "threat for money", "demand money", "blackmail"],
        "offenceSection": "BNS Section 308",
        "punishmentSection": "BNS Section 308",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Threat messages", "Call records", "Bank records", "Witness statements"]
    },

    # 165
    {
        "id": 165,
        "case": "Robbery",
        "keywords": ["robbery", "rob", "armed robbery", "force theft"],
        "offenceSection": "BNS Section 309",
        "punishmentSection": "BNS Section 309",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Weapon", "Stolen property", "Witness statements"]
    },

    # 166
    {
        "id": 166,
        "case": "Dacoity",
        "keywords": ["dacoity", "dacoit", "gang robbery", "five persons robbery"],
        "offenceSection": "BNS Section 310",
        "punishmentSection": "BNS Section 310",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Weapons", "Communication records", "Witness statements"]
    },

    # 167
    {
        "id": 167,
        "case": "Robbery or dacoity with attempt to cause death or grievous hurt",
        "keywords": ["robbery serious injury", "dacoity attack", "robbery with weapon"],
        "offenceSection": "BNS Section 311",
        "punishmentSection": "BNS Section 311",
        "punishment": "Punishment as provided by BNS Section 311",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Medical report", "Weapon", "CCTV", "Forensic evidence"]
    },

    # 168
    {
        "id": 168,
        "case": "Attempt to commit robbery or dacoity while armed",
        "keywords": ["armed robbery attempt", "deadly weapon robbery", "attempt dacoity"],
        "offenceSection": "BNS Section 312",
        "punishmentSection": "BNS Section 312",
        "punishment": "Punishment as provided by BNS Section 312",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Weapon", "CCTV", "Witness statements"]
    },

    # 169
    {
        "id": 169,
        "case": "Belonging to gang of robbers or dacoits",
        "keywords": ["gang robber", "gang dacoit", "robbery gang", "dacoity gang"],
        "offenceSection": "BNS Section 313",
        "punishmentSection": "BNS Section 313",
        "punishment": "Punishment as provided by BNS Section 313",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Communication records", "Financial records", "Witness statements"]
    },

    # 170
    {
        "id": 170,
        "case": "Dishonest misappropriation of property",
        "keywords": ["misappropriation", "wrongfully use property", "property misuse"],
        "offenceSection": "BNS Section 314",
        "punishmentSection": "BNS Section 314",
        "punishment": "Punishment as provided by BNS Section 314",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Ownership records", "Transaction records", "Documents"]
    },

    # 171
    {
        "id": 171,
        "case": "Misappropriation of deceased person's property",
        "keywords": ["deceased property", "inheritance property", "dead person's property"],
        "offenceSection": "BNS Section 315",
        "punishmentSection": "BNS Section 315",
        "punishment": "Punishment as provided by BNS Section 315",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Will", "Property records", "Bank records"]
    },

    # 172
    {
        "id": 172,
        "case": "Criminal breach of trust",
        "keywords": ["breach of trust", "entrusted property", "entrusted money", "misuse entrusted property"],
        "offenceSection": "BNS Section 316",
        "punishmentSection": "BNS Section 316",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Agreement", "Bank records", "Receipts", "Messages"]
    },

    # 173
    {
        "id": 173,
        "case": "Stolen property",
        "keywords": ["stolen property", "receive stolen goods", "retain stolen property"],
        "offenceSection": "BNS Section 317",
        "punishmentSection": "BNS Section 317",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Recovered property", "Purchase records", "Messages"]
    },

    # 174
    {
        "id": 174,
        "case": "Cheating",
        "keywords": ["cheating", "fraud", "deceive", "cheated", "online fraud"],
        "offenceSection": "BNS Section 318",
        "punishmentSection": "BNS Section 318",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Messages", "Bank records", "Agreements", "Transaction records"]
    },

    # 175
    {
        "id": 175,
        "case": "Cheating by personation",
        "keywords": ["personation", "fake identity", "identity fraud", "pretend someone else"],
        "offenceSection": "BNS Section 319",
        "punishmentSection": "BNS Section 319",
        "punishment": "Punishment as provided by BNS Section 319",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Identity documents", "Messages", "Digital records", "Bank records"]
    },

    # 176
    {
        "id": 176,
        "case": "Fraudulent removal of property to prevent distribution",
        "keywords": ["hide property from creditors", "fraudulent property removal", "hide assets"],
        "offenceSection": "BNS Section 320",
        "punishmentSection": "BNS Section 320",
        "punishment": "Punishment as provided by BNS Section 320",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Property records", "Bank records", "Transfer documents"]
    },

    # 177
    {
        "id": 177,
        "case": "Dishonestly preventing debt from being available to creditors",
        "keywords": ["hide assets creditors", "prevent creditor recovery", "debt fraud"],
        "offenceSection": "BNS Section 321",
        "punishmentSection": "BNS Section 321",
        "punishment": "Punishment as provided by BNS Section 321",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Financial records", "Property documents", "Bank transactions"]
    },

    # 178
    {
        "id": 178,
        "case": "Dishonest execution of deed with false consideration",
        "keywords": ["false property deed", "fake consideration", "fraudulent deed"],
        "offenceSection": "BNS Section 322",
        "punishmentSection": "BNS Section 322",
        "punishment": "Punishment as provided by BNS Section 322",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Property deed", "Registration records", "Bank records"]
    },

    # 179
    {
        "id": 179,
        "case": "Dishonest or fraudulent removal or concealment of property",
        "keywords": ["hide property", "fraudulent property transfer", "conceal property"],
        "offenceSection": "BNS Section 323",
        "punishmentSection": "BNS Section 323",
        "punishment": "Punishment as provided by BNS Section 323",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Property records", "Transfer documents", "Financial records"]
    },

    # 180
    {
        "id": 180,
        "case": "Mischief",
        "keywords": ["mischief", "damage property", "destroy property", "property damage"],
        "offenceSection": "BNS Section 324",
        "punishmentSection": "BNS Section 324",
        "punishment": "Punishment depends on subsection and amount/type of damage",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Photographs", "CCTV", "Repair estimate", "Witness statements"]
    },

    # 181
    {
        "id": 181,
        "case": "Mischief by killing or maiming animal",
        "keywords": ["kill animal", "maim animal", "animal property damage"],
        "offenceSection": "BNS Section 325",
        "punishmentSection": "BNS Section 325",
        "punishment": "Punishment as provided by BNS Section 325",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Veterinary report", "Photographs", "Witness statements"]
    },

    # 182
    {
        "id": 182,
        "case": "Mischief by fire, explosive or inundation",
        "keywords": ["fire property damage", "explosive property damage", "flood property damage"],
        "offenceSection": "BNS Section 326",
        "punishmentSection": "BNS Section 326",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Fire report", "Forensic evidence", "CCTV", "Damage report"]
    },

    # 183
    {
        "id": 183,
        "case": "Mischief affecting railway, aircraft or vessel",
        "keywords": ["railway damage", "aircraft damage", "ship damage", "transport sabotage"],
        "offenceSection": "BNS Section 327",
        "punishmentSection": "BNS Section 327",
        "punishment": "Punishment as provided by BNS Section 327",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Forensic report", "Transport records"]
    },

    # 184
    {
        "id": 184,
        "case": "Intentionally running vessel aground",
        "keywords": ["run vessel aground", "ship sabotage", "vessel theft"],
        "offenceSection": "BNS Section 328",
        "punishmentSection": "BNS Section 328",
        "punishment": "Punishment as provided by BNS Section 328",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Navigation records", "CCTV", "Witness statements"]
    },

    # 185
    {
        "id": 185,
        "case": "Criminal trespass and house-trespass",
        "keywords": ["criminal trespass", "house trespass", "illegal entry", "enter property"],
        "offenceSection": "BNS Section 329",
        "punishmentSection": "BNS Section 329",
        "punishment": "Punishment depends on subsection",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Property documents", "Witness statements"]
    },

    # 186
    {
        "id": 186,
        "case": "House-trespass and house-breaking",
        "keywords": ["house breaking", "break into house", "burglary", "house breaking"],
        "offenceSection": "BNS Section 330",
        "punishmentSection": "BNS Section 330",
        "punishment": "Punishment as provided by BNS Section 330",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Broken lock", "CCTV", "Fingerprints", "Tools"]
    },

    # 187
    {
        "id": 187,
        "case": "Punishment for house-trespass or house-breaking",
        "keywords": ["house trespass punishment", "house breaking punishment", "burglary punishment"],
        "offenceSection": "BNS Section 331",
        "punishmentSection": "BNS Section 331",
        "punishment": "Punishment depends on subsection and circumstances",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Broken locks", "Fingerprints", "Recovered property"]
    },

    # 188
    {
        "id": 188,
        "case": "House-trespass to commit an offence",
        "keywords": ["enter house to commit crime", "house trespass offence", "illegal house entry"],
        "offenceSection": "BNS Section 332",
        "punishmentSection": "BNS Section 332",
        "punishment": "Punishment depends on the intended offence and subsection",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["CCTV", "Tools", "Witness statements", "Forensic evidence"]
    },

    # 189
    {
        "id": 189,
        "case": "House-trespass after preparation for hurt or assault",
        "keywords": ["house trespass weapon", "break in with weapon", "house attack"],
        "offenceSection": "BNS Section 333",
        "punishmentSection": "BNS Section 333",
        "punishment": "Punishment as provided by BNS Section 333",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Weapon", "CCTV", "Broken door", "Witness statements"]
    },

    # 190
    {
        "id": 190,
        "case": "Dishonestly breaking open receptacle containing property",
        "keywords": ["break locker", "break safe", "break container", "open locked box"],
        "offenceSection": "BNS Section 334",
        "punishmentSection": "BNS Section 334",
        "punishment": "Punishment depends on subsection",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Broken lock", "Container", "CCTV", "Fingerprints"]
    },

    # 191
    {
        "id": 191,
        "case": "Making a false document",
        "keywords": ["fake document", "false document", "create fake document", "document forgery"],
        "offenceSection": "BNS Section 335",
        "punishmentSection": "BNS Section 335",
        "punishment": "Punishment as provided by BNS Section 335",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Document", "Digital metadata", "Signature", "Forensic examination"]
    },

    # 192
    {
        "id": 192,
        "case": "Forgery",
        "keywords": ["forgery", "forge document", "fake signature", "fake certificate"],
        "offenceSection": "BNS Section 336",
        "punishmentSection": "BNS Section 336",
        "punishment": "Punishment depends on subsection and type of document",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Original document", "Forensic report", "Signature analysis", "Digital records"]
    },

    # 193
    {
        "id": 193,
        "case": "Forgery of Court record or public register",
        "keywords": ["forge court record", "fake public register", "fake court document"],
        "offenceSection": "BNS Section 337",
        "punishmentSection": "BNS Section 337",
        "punishment": "Punishment as provided by BNS Section 337",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Court records", "Register", "Forensic examination"]
    },

    # 194
    {
        "id": 194,
        "case": "Forgery of valuable security, will or important document",
        "keywords": ["fake will", "fake valuable security", "forged will", "document forgery"],
        "offenceSection": "BNS Section 338",
        "punishmentSection": "BNS Section 338",
        "punishment": "Punishment as provided by BNS Section 338",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Will", "Financial document", "Signature analysis", "Forensic report"]
    },

    # 195
    {
        "id": 195,
        "case": "Possession of forged document with intent to use it as genuine",
        "keywords": ["possess forged document", "keep fake document", "use forged document"],
        "offenceSection": "BNS Section 339",
        "punishmentSection": "BNS Section 339",
        "punishment": "Punishment as provided by BNS Section 339",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Forged document", "Device records", "Messages", "Forensic report"]
    },

    # 196
    {
        "id": 196,
        "case": "Using forged document or electronic record as genuine",
        "keywords": ["use fake document", "use forged certificate", "fake electronic record"],
        "offenceSection": "BNS Section 340",
        "punishmentSection": "BNS Section 340",
        "punishment": "Punishment as provided by BNS Section 340",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Forged document", "Electronic record", "Device forensic report"]
    },

    # 197
    {
        "id": 197,
        "case": "Making or possessing counterfeit seal for forgery",
        "keywords": ["fake seal", "counterfeit seal", "fake stamp", "counterfeit stamp"],
        "offenceSection": "BNS Section 341",
        "punishmentSection": "BNS Section 341",
        "punishment": "Punishment as provided by BNS Section 341",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Counterfeit seal", "Tools", "Forensic examination"]
    },

    # 198
    {
        "id": 198,
        "case": "Making or possessing counterfeit seal for other forgery",
        "keywords": ["counterfeit seal", "fake official seal", "fake stamp"],
        "offenceSection": "BNS Section 342",
        "punishmentSection": "BNS Section 342",
        "punishment": "Punishment as provided by BNS Section 342",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Fake seal", "Tools", "Forensic report"]
    },

    # 199
    {
        "id": 199,
        "case": "Fraudulent cancellation or destruction of will or valuable security",
        "keywords": ["destroy will", "cancel valuable security", "destroy legal document"],
        "offenceSection": "BNS Section 343",
        "punishmentSection": "BNS Section 343",
        "punishment": "Punishment as provided by BNS Section 343",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Original document", "Document history", "Witness statements"]
    },

    # 200
    {
        "id": 200,
        "case": "Falsification of accounts",
        "keywords": ["false accounts", "fake accounts", "account falsification", "financial records fraud"],
        "offenceSection": "BNS Section 344",
        "punishmentSection": "BNS Section 344",
        "punishment": "Punishment as provided by BNS Section 344",
        "classification": "See BNSS First Schedule",
        "court": "See BNSS First Schedule",
        "evidence": ["Accounting records", "Bank statements", "Invoices", "Digital records"]
    }

]
@app.route("/")
def home():
    return render_template("indexs.html")


@app.route("/search", methods=["GET"])
def search_case():

    query = request.args.get("query", "").lower().strip()

    if not query:
        return jsonify([])

    results = []

    for case in legalCases:

        if query in case["case"].lower():
            results.append(case)
            continue

        for keyword in case["keywords"]:

            if query in keyword.lower() or keyword.lower() in query:
                results.append(case)
                break

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)