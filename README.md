1) توصيف الحالة
لدي رقعة ابعادها n*n تم تمثيل الخلايا فيها عن طريق class cell
و class cell يوجد فيه ثلاث انواع للخلايا وهي normal,blocke,target
وممكن ان اضع احجارا فوق الخلايا الفارغة
يوجد لدي class للاحجار وهو class stone يوجد فيه ثلاث انواع للاحجار blue ,redd,iron

2) فضاء الحالات:
تمثل الشبكة 
𝑛
×
𝑛
n×n بحالتها الكاملة (نوع كل خلية ومحتواها).
مواقع الأحجار (الزرقاء، الحمراء، والعادية) على الشبكة.
حركات ممكنة:

تحريك الأحجار المغناطيسية الزرقاء والحمراء فقط إلى خلايا فارغة.
تطبيق التنافر أو التجاذب حسب نوع المغناطيس بعد كل حركة.
قيود على الحالة:

لا يمكن وضع حجر على خلية blocked.
كل خلية تحتوي على نوع واحد فقط من الأحجار أو تكون فارغة.
الوصول إلى الهدف:

تكون كل خلايا target تحتوي على أحجار (زرقاء، حمراء، أو عادية)


3) الحالة الابتدائية
تكون الحالة الايتدائية رقعة مقسمة لخلايا وممكن ان يكون فوقها مغناطيس ازرق او احمر او الاثنين معا بالضافة الى احجار عادية 
الخلية الافتراضية يكون نوعها normal
ويوجد خلايا target وممكن ان يوجد خلايا blocke
يتم وضع الاحجار على الخلايا باستخدام تابع  place_stone

4)العمليات والاجراءات
لدي التوابع الاتية:
تابع move_stone:
هذا التابع ينقل فقط الاحجار المغناطيسية واذا كان الحجر عادي لا ينقله
ويتحقق من الخلية اذا كانت فارغة اي لا يوجد فيها حجر سواء كانت الخلية المصدر او الوجهة
تابع apply_repulsion:
هو تابع التنافر ومسؤول عن نفر الاحجار العادية او المغناطيس الاحمر الموجودين على صف او عمود المغناطيس الازرق بعد تحريكه
تابع apply_attraction:
وهو تابع التجاذب ومسؤول عن جذب الاحجار العادية او المغناطيس الازرق الموجودة على صف او عمود المغناطيس الاحمر بعد تحريكه
تابع check_win:
هو تابع اختبار الفوز يمر على كل صف بالرقعة وكل خلية بالصف الواحدويتحقق اذا كان نوعها 
target
وموجود فيها حجر اي ليست فارغة 
اذا كانت كل الtarget محققة للشرط فانني فزت 
تابع setup_level:
لانشاء مرحلة
تابع play_level

5) الحالة النهائية
تكون كل الخلايا الهدف اي ال target يوجد فيها احجار عادية او مغناطيس ازرق او احمر 

خوارزمية ال bfs:
بنية المعطيات: queue
الية الحل:
اولا نضع الجالة الاولية في الqueue
يتم اخذ الحالةالحالية من مقدمة ال queue
ونتحقق من الحالة الحالية اذا كانت تحقق الهدف (check_win)
اذا كانت تحقق الهدف نطبع المسار الى الهدف ونعرض الحركات المطلوبة ويتم انهاء البحث
واذا لم تحقق الحالة الهدف نمثل الحالة كحالة متسلسلة باستخدام قيم الاحجار في الشبكة
اذا كانت مزارة من قبل نتخطاها واذا كانت جديدة تضاف الى قائمة الحالات المزارة
يتم تحديد جميع التحركات الممكنة للاحجار الزرقاء والحمراء
كل حركة مسموحة تؤدي الى انشاء حالة جديدة
تضاف الحالة الجديدة الى ال queue مع المسار الجديد 
الحل:
عند ايجاد الحل تتم طباعة المسار مع الحركات المطلوبة لتحقيق الهدف ويتم عرض كل خطوة بالتفصيل 
يتم تحديد الخلية المصدر والخلية الوجهة 
يتم عرض ال board بعد كل حركة 

خوارزمية ال dfs:
بنية المعطيات :stack
الية الحل:
اولا نضع الحالة الاولية في stack
يتم اخذ الحالة الاولية من ال stack ويتم التحقق مما اذا كانت الحالة الحالية تحقق الهدف 
............................................................................................................. ونكمل كما في ال bfs

الحل : نفس ال bfs
