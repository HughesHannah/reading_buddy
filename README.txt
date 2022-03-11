if delete the db and migration file, should create a new superuser:
~$ python manage.py createsuperuser
And also if there are some changes of the model.py or database, migrate it.
~$ python manage.py makemigrations rango
~$ python manage.py migrate
~$ python populate_rango.py
~$ python manage.py createsuperuser

superusername: 111
pwd: apple1234

****************************************************************************************
populate data:
Categories:  Arts    Computing   History    Literature

Books:
Arts:    
Small Pleasures   Clare Chambers   Longlisted for the Women's Prize for Fiction 2021
Still Life   Sarah Winman   The instant Sunday Times bestseller and BBC Between the Covers Book Club pick
Scenic Painting    Kevin Todd   33 Kinds of Watercolor Painting Techniques Completely Self-learning Tutorial

Computing:
Excel 2021  Martin Jackson  A Step by Step Beginners Course to Master Microsoft Excel Through Exercises and Illustrations, both for Windows and Mac
Ultimate Guide to Twitter for Business  Ted Prodromou  Generate Quality Leads Using Only 140 Characters, Instantly Connect with 300 million Customers in 10 Minutes..
The Simulated Multiverse   Rizwan Virk   An MIT Computer Scientist Explores Parallel Universes, The Simulation Hypothesis, Quantum Computing and the Mandela Effect

History:
The Burgundians: A Vanished Empire   Bart Van Loo   A history book that reads like a thriller
Ancestors: A prehistory of Britain in seven burials   Alice Roberts   An extraordinary exploration of the ancestry of Britain through seven burial sites. 
Hamilton: The Revolution    Lin-Manuel Miranda    Winner of the 2016 Pulitzer Prize for Drama

Literature:
I Have Something to Tell You   Susan Lewis    The most thought-provoking, captivating fiction novel of 2021 from bestselling author Susan Lewis
Bamburgh   LJ Ross   A DCI Ryan Mystery (The DCI Ryan Mysteries Book 19)
The Four Winds    Kristin Hannah   The Internationally Bestselling Richard & Judy Book Club Pick

   