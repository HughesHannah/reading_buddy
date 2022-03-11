import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reading_buddy.settings')

import django
django.setup()
from rango.models import Category, Book, Comment, UserProfile, ReadingList
from django.contrib.auth.models import User

def populate():
    Arts_Book=[
        {'book_name':'Small Pleasures',
        'author':'Clare Chambers ',
        'intro':'Longlisted for the Womens Prize for Fiction 2021',
        'likes':19,
        'views':37,
        'score':8.2,
        'content':'Teeming with unforgettable characters and oozing atmosphere, it is a joyous, summery ode to love, art and poetry'
        },
        {'book_name':'Still Life',
        'author':'Sarah Winman',
        'intro':'The instant Sunday Times bestseller and BBC Between the Covers Book Club pick',
        'likes':24,
        'views':46,
        'score':7.3,
        'content':'A gorgeous, generous story of kind hearts and kindred spirits redefining the meaning of family and friendship'},
        {'book_name':'Scenic Painting',
        'author':'Kevin Todd',
        'intro':'33 Kinds of Watercolor Painting Techniques Completely Self-learning Tutorial',
        'likes':31,
        'views':47,
        'score':8.6,
        'content':'A wonderful novel. I loved it.'}
    ]

    Computing_Book=[
        {'book_name':'Excel 2021',
        'author':'Martin Jackson',
        'intro':'A Step by Step Beginners Course to Master Microsoft Excel Through Exercises and Illustrations, both for Windows and Mac',
        'likes':37,
        'views':59,
        'score':7.7,
        'content':'This book comes with some little quizzes, which test your theoretical knowledge about excel'},
        {'book_name':'Ultimate Guide to Twitter for Business',
        'author':'Ted Prodromou',
        'intro':'Generate Quality Leads Using Only 140 Characters, Instantly Connect with 300 million Customers in 10 Minutes..',
        'likes':41,
        'views':46,
        'score':7.1,
        'content':'The book is ok, it sows some concepts but I wanted a book that explains how the campaigns and Twitter ads actual work. '},
        {'book_name':'The Simulated Multiverse',
        'author':'Rizwan Virk',
        'intro':'An MIT Computer Scientist Explores Parallel Universes, The Simulation Hypothesis, Quantum Computing and the Mandela Effect',
        'likes':31,
        'views':57,
        'score':7.5,
        'content':'Best practices for designing and managing worksheets'}
    ]


    History_Book=[
        {'book_name':'The Burgundians: A Vanished Empire',
        'author':'Bart Van Loo',
        'intro':'A history book that reads like a thriller',
        'likes':28,
        'views':49,
        'score':8.9,
        'content':'History told – and well told, too – for those who value narrative at least as much as the finicky details of economics or treaty-making'},
        {'book_name':'Ancestors: A prehistory of Britain in seven burials',
        'author':'Alice Roberts',
        'intro':'An extraordinary exploration of the ancestry of Britain through seven burial sites.',
        'likes':35,
        'views':61,
        'score':7.0,
        'content':'I was very disappointed with this book. I have seen the good Prof on stage a couple of times, and enjoyed them both. Her TV shows are always worth a watch.'},
        {'book_name':'Hamilton: The Revolution',
        'author':'Lin-Manuel Miranda',
        'intro':'Winner of the 2016 Pulitzer Prize for Drama',
        'likes':32,
        'views':46,
        'score':9.1,
        'content':'Absolutely excellent. Clearly and concisely written and utterly fascinating.'}
    ]

    Literature_Book=[
        {'book_name':'I Have Something to Tell You',
        'author':'Susan Lewis',
        'intro':'The most thought-provoking, captivating fiction novel of 2021 from bestselling author Susan Lewis',
        'likes':47,
        'views':59,
        'score':8.6,
        'content':'I was hooked by the suspenseful plotting, depth of character and legal backdrop. This is a deep book which I greatly enjoyed. Rather like an appetite-wetting five course meal with a surprise menu'},
        {'book_name':'Bamburgh',
        'author':'LJ Ross',
        'intro':'A DCI Ryan Mystery (The DCI Ryan Mysteries Book 19)',
        'likes':39,
        'views':61,
        'score':6.7,
        'content':'Movingly written and plotted with the skill of Greek tragedy. You’ll keep turning the pages until the last racking sob'},
        {'book_name':'The Four Winds',
        'author':'Kristin Hannah',
        'intro':'The Internationally Bestselling Richard & Judy Book Club Pick',
        'likes':33,
        'views':48,
        'score':8.2,
        'content':'Wow. I have been left with a bursting heart . . . a story of love, family, unbreakable bonds, bravery and hope. I will never forget the characters, what they endured and how they hoped and loved. I feel that I will be forever touched by them. I loved this book so much! '}
    ]


    '''
    Book1_comment=[
        {'content':'Small Pleasures is no twee romance, but a quietly compelling novel of duty and desire'},
        {'content':'A wonderful novel. I loved it.'}
    ]
    
    Book2_comment=[
        {'content':'Teeming with unforgettable characters and oozing atmosphere, it’s a joyous, summery ode to love, art and poetry'},
        {'content':'A gorgeous, generous story of kind hearts and kindred spirits redefining the meaning of family and friendship'}
    ]

    Book3_comment=[
        {'content':'This book comes with some little quizzes, which test your theoretical knowledge about excel'},
        {'content':'Best practices for designing and managing worksheets'}
    ]

    Book4_comment=[
        {'content':'The book is ok, it sows some concepts but I wanted a book that explains how the campaigns and Twitter ads actual work. '},
        {'content':'One of the most complete books on Twitter you wll find.'}
    ]

    Book5_comment=[
        {'content':'History told – and well told, too – for those who value narrative at least as much as the finicky details of economics or treaty-making'},
        {'content':'The political and the personal, economics and culture, belief and violence, success and failure, major developments and spicy details – it is all there'}
    ]

    Book6_comment=[
        {'content':'I was very disappointed with this book. I have seen the good Prof on stage a couple of times, and enjoyed them both. Her TV shows are always worth a watch.'},
        {'content':'Absolutely excellent. Clearly and concisely written and utterly fascinating.'}
    ]

    Book7_comment=[
        {'content':'An intriguing read that drew me in from the very beginning. It combines heartfelt family drama with a gripping plot. The characters are expertly drawn …'},
        {'content':'I was hooked by the suspenseful plotting, depth of character and legal backdrop. This is a deep book which I greatly enjoyed. Rather like an appetite-wetting five course meal with a surprise menu'}
    ]

    Book8_comment=[
        {'content':'Wow. I have been left with a bursting heart . . . a story of love, family, unbreakable bonds, bravery and hope. I will never forget the characters, what they endured and how they hoped and loved. I feel that I will be forever touched by them. I loved this book so much! '},
        {'content':'Movingly written and plotted with the skill of Greek tragedy. You’ll keep turning the pages until the last racking sob'}
    ]

    '''

    cats = {'Arts': {'Book':Arts_Book},
            'Computing': {'Book':Computing_Book},
            'History': {'Book':History_Book},
            'Literature': {'Book':Literature_Book}, }


    '''
    Books = {'Small Pleasures': {'Comment':Book1_comment},
            'Still Life':{'Comment':Book2_comment},
            'Excel 2021':{'Comment':Book3_comment},
            'Ultimate Guide to Twitter for Business':{'Comment':Book4_comment},
            'The Burgundians: A Vanished Empire':{'Comment':Book5_comment},
            'Ancestors A prehistory of Britain in seven burials':{'Comment':Book6_comment},
            'I Have Some thing to Tell You':{'Comment':Book7_comment},
            'The Four Winds':{'Comment':Book8_comment},}
    '''

    user = User.objects.get_or_create(username='test',email='test.qq.com')[0]
    user.set_password('123456')
    user.save()

    profile = UserProfile.objects.get_or_create(user=user)[0]
    profile.save()

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for q in cat_data['Book']:
            b = add_Book(c, q['book_name'], q['author'],q['intro'], likes=q['likes'], views=q['views'], score=q['score'])
            add_comment(b,q['content'])

    add_reading()
    for c in ReadingList.objects.all():
        print(f'{c}')
    
    
    for c in Category.objects.all():
        for q in Book.objects.filter(category=c):
            print(f'- {c}: {q}')


    for c in Book.objects.all():
        for q in Comment.objects.filter(Book=c):
            print(f'- {c}: {q}')    
    
    
    '''
   for c in comments:
        addComment(question_id=c['question_id'], content=c['content'])
        
     '''
    

def add_Book(cat, book_name,author, intro, likes, views,score): 
    q = Book.objects.get_or_create(category=cat, book_name=book_name)[0]
    q.author=author
    q.intro=intro
    q.likes=likes
    q.views=views
    q.score=score
    q.save()
    return q

def add_cat(cat_name):
    c = Category.objects.get_or_create(cat_name=cat_name)[0]
    c.save()
    return c

def add_comment(Book,content):
    o = Comment.objects.get_or_create(Book=Book, content = content,user_id=1)[0]
    o.save()
    return o

def add_reading():
    r = ReadingList.objects.get_or_create(user_id=1)[0]
    r.book1='Small Pleasures'
    r.book2='Still Life'
    r.book3='Ultimate Guide to Twitter for Business'
    r.book4='Excel 2021'
    r.book5='The Four Winds'
    r.save()
    return r


'''
def addComment(question_id,content):
    c = Comment.objects.get_or_create(question_id=question_id,content=content,user_id=1)[0]
    c.save()
 '''


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()