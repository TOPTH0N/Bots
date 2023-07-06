from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدأ استـخـراج الجـلسة", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجـوع 🔙", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "سـوࢪس أكـس ستريم", url="https://t.me/xXStrem"
            )
        ],
        [
            InlineKeyboardButton("- كيـفـية اެݪاستـخـدام", callback_data="help"),
            InlineKeyboardButton("- حـول", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور", url="https://t.me/zQQQzQ")],
    ]

    START = """
مـࢪحبـًا عـزيـزي  {}
أنـا مـخـصـص لاسـتخـࢪاج اެݪجـلـسات
بـايـࢪوجࢪام أو تـيـࢪمـكس
للبـدء في الاسـتـخࢪاج اضغط بدأ استـخࢪاج اެݪجـلـسة
المطوࢪ  : @zQQQzQ
    """

    HELP = """
 **الأوامࢪ المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ࢪيبو البوت
/generate - لاستخࢪاج الجلسات 
/cancel - لإلغاء الاستخࢪاج 
/restart - لتࢪسيت اليوت
"""

    # About Message
    ABOUT = """
**حول البوت** 

مـࢪحبـًا عـزيـزي أنا هـنا لاسـتـخࢪاج الجـلـسات بـࢪمـجـة المطـوࢪ @zQQQzQ

قناة السوࢪس : [᥉᥆ᥙᖇᥴᥱ ꪎꪎ᥉ƚᖇᥱꪔ](https://t.me/xXStrem)
لغة البـرمـجـة : [بـايروجرام](docs.pyrogram.org)
اللغة : [بايثون](www.python.org)
المـطـور : @zQQQzQ
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
صـل على النبي 🤍  
┏━━━━━━━━━━━━━━━━━┓
┣★ قـناة مطـوري . [🤍](https://t.me/D8BB8)
┣★ الـمطور : [اضغط هنا](https://t.me/zQQQzQ)
┣★ السـورس [ ᥉᥆ᥙᖇᥴᥱ ꪎꪎ᥉ƚᖇᥱꪔ](https://t.me/xXStrem)
┗━━━━━━━━━━━━━━━━━┛
💞 
إذا كان لديك أي سؤال ، فࢪاسل » المطوࢪ » [المـطور] @zQQQzQ
   """
