سلام
خیلی خوب  کامنت نذاشتم در هر حال لذت ببرید به عبارتی اصول رو در کامنت رعایت نکردم
@pouriashafiee
I Love Python & Java
-----------------------
'''
    \f ابتدا فایل README رو مطالعه کنید
    '''
    # Example1 :
    # دیونه -> دیوانه
    # شما میتونین حتی یک جمله بنویسید دقت کنید جملتونو شکیل بنویسید
    obj = FormalConverter()
    a = obj.get_formal_converter()
    print(a)
    # ------------
    # Example 2 :
    # کلاس و متد های زیر یه متن بهش میدید و واستون جمله های اون متن رو مشخص میکنه و جدا میکند
    obj = IdentifySentencesSimple()
    a = obj.getـisolatedـlist()
    b = obj.get_list_identify_sentences()
    print(a, b)
    # ------------------------------
    # Example 3 :
    # کلاس و متد زیر هم به این صورت هست که یه کلمه یا جمله بهش میدید و بهتون میگه که حس منفی داره یا مثبت یا خنثی
    '''
        گاهی به درستی تشخیص نمیده :))
    '''
    obj3 = SensoryAnalysis()
    print(obj3.get_sence_sentence())
    # ---------------------
    # Example 4 :
    # بدین صورت کار میکنه که یه متن بهش میدید و بهتون میگه چند تا فحش دادید :|
    # بدرد این میخوره که توی سیستم نظرات فیلتر کنه
    obg4 = RecognizeVulgarWords()
    result = obg4.get_recognize_vulgar_words()
    print(result)