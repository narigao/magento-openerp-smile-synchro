# Python and OpenERP - why #
Anybody with say 2 years of experience in any object oriented language like Java, PHP5 or C++ is able to catch up with the minimum required level of Python programming for OpenERP in one to two weeks. Beginners can even start on Python although they will need more time.

Also bare in mind that despite not being that popular Python is one of the simplest object oriented programming language around. It's probably because Python states "there should be only one way to do things". Python is also a good trade-off between a first class OOP abstraction and a good speed: almost an order of magnitude faster than PHP (while still being an order of magnitude slower than Java or C++; there is no free lunch). Of course, those are only algorithmic considerations. Better productivity leading to more time for architectural or database optimizations always make more difference. And Python is still rising in popularity, reaching [rank #6 in the famous Tiobe index](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html).

Also, believe my deep comparison or check by yourself, OpenERP requires somewhat 10 times less code than Java ERP's around to do the same functional stuff (let's call those two "Java based" even if they are actually more like PSQL/procedural coding oriented, at least for their business code layer, which unfortunately is the one that matters) Needless to say OpenERP actually does much more instead. Just investigate data migration, cost of customization, versatility, fixtures loading, project management, CRM, complex stock management...

Finally, this would be quite off-topic, but I think the key why Python or any good Dynamic OOP language (like (J)Ruby) is the good choice to build an ERP is because an ERP really needs both functional flexibility and a good relational database persistence system. But achieving both modularity, runtime data model flexibility and a static language like Java is really a hard thing that real Java ERP's generally failed to achieve so far.

Indeed, in a static language, the OOP model, mapped to the database structure is supposed to be mostly fixed at compilation time. Gaining runtime flexibility like with the application dictionary of Compiere or Openbravo means too often losing some OOP power like inheritability or encapsulation. Oh yes that would still be possible, but that would mean over-engineering an ERP platform just like OSGI or the Eclipse RCP. Ultimately, you'll find guys able to do that. But will they do it as open source and will they master also the functional part of an ERP? Quite unlikely. So choosing a static language as the main language for an ERP results either in non functional/non mature boiler plate code, either functional code that is really to badly designed to fit any different context without a ton of non maintainable coding. So a dynamic OOP language is the good choice, at least for the business layer of an ERP.

Also, for those fearing runtime errors in OpenERP because it uses a dynamic language, I would say that in OpenERP:
  * there is roughly 5 times less code than is an equivalent Java language based code, or even 10 times less code than a procedural ERP like SAP, Openbravo or Compiere. So that's much less code to watch for the same features. Also bare in mind that PLSQL, HSQL, JSP, XML IOC like Spring and all those usual techs won't provide you more static security either: they are dynamic stuff too even if they are bad at OOP.
  * OpenERP comes with some unit and functional testing.
  * The compiler might do less work, there is a huge community testing the software, that's valid too.

So Finally, a dynamic language such as Python is a very good choice for an ERP. The runtime errors that might occur will always be discovered and fixed at implementation time, so they will not be a trouble at runtime.


# Why the hell didn't they used Rails instead? #
Well, first you might know that Python and Ruby are really close, almost as close as C# and Java. No question Rails is an outstanding framework. But building a full blown ERP is not an easy task, building a business mature ERP won't take less than 3 years. This is not only about getting the technical platform right (while that's a minimal condition and I predict resounding failures of leading brands because they didn't really passed that first stage), this is also about getting all the functional right, and since the functional stuff is too large for a unique open source team, this is even about getting a true (unlike some hyped oss products around) community catalysis right. OpenERP achieved all that, no too shabby.

Second, if you take a look to the underlining [OpenObject framework](http://openobject.com/), you'll see lots of things that are similar to Rails, here are a few ones:
  * the ORM is dynamic ActiveRecord pattern, with similar extra features like single and multiple table inheritance and associations.
  * ORM with two cache levels since OpenERP 5. Almost as good as Java Hibernate, but much easier and versatile...
  * the code is very DRY all the way. Not a single duplicated line.
  * MVC architecture.
  * Stateless design. Rails wins here because it's also fully HTTP REST compliant while OpenERP doesn't benefit yet the idempotence of most of HTTP methods and use HTTP POST instead to tunnel its XML/RPC, while also supporting the fast NetRPC protocol (similar to Java RMI) or HTTP via eTiny, more specifically a thin Turbogears/CherryPy layer), but that's not as RESTful as Rails yet.
  * fixtures with several formats (CSV, XML, no Yaml yet) with fixture relative ids like in Rails 2.x which make loading demo or config data a piece of cake unlike with other ERP's.
  * no HQL or yet an other scripting SQL language wrapper like Hibernate, but, just like the Rails [ActiveRecord](http://ar.rubyonrails.org/) philosophy a simple CRUD ORM API + an easy way to fire custom pure SQL request whenever it's required.
  * built'in unit test infrastructure. Not as good as Rspec, but hundred times better than what other ERP's offer.
  * Unlike Rails, [OpenERP views](http://openerp.com/wiki/index.php/Developers:Developper%27s_Book/The_views) are a pure XML simple widget components oriented dialect with no interpreted code inside. That's because an ERP doesn't claim to be as flexible as a shiny web2.0 HTML page but rather focus on productivity inside the ERP interface paradigm. Still, the eTiny extra layer can offer that flexibility if you really want too.

So finally, yes, I'm convinced Rails would have been better. But let's face it:
  1. Rails was not available yet when OpenERP has been built.
  1. Rails would boost ERP productivity by say 10% only. But running 10% faster while starting 5 years late would make absolutely no difference at the end; this is really not like running 5 times faster than the Java language and starting almost at the same time. So I believe 10% this is not enough to make the difference considering all the other involved factors like functional perimeter, quality of the governance, community momentum...

Finally Python and OpenObject are by far good enough for OpenERP to be the best ERP around, and I would bet quite heavily that no product will ever pass it in the coming next 5 years at least, this is very much written already.

# Python howto #
So now that you are all the more convinced OpenERP made very reasonable choices, you'll eventually need to learn Python a bit. Don't panic that's very easy.
You'll need to read an practice the following tutorials during say a week if starting from scratch:
http://www.diveintopython.org/toc/index.html
Not all Python knowledge is required to understand 90% of OpenERP code.
Just focus on chapter 1 to 5 included. Chapter 6 might occasionally be useful if you need to deal with files.


# OpenERP howto #
First, look at the demos:
http://openerp.com/demonstration.html
(also the flash based demos)
http://www.openobject.com/index.php?option=com_content&task=view&id=30&Itemid=72

Now dive into the OpenObject framework, again practicing during roughly a week:
Old but still 99% valid and simple tutorial: http://openerp.com/wiki/index.php/Developers:MinutesCustom/HomePage
full doc:
http://doc.openerp.com/developer/index.html#book-develop-link

# IDE howto #
Install Eclipse and the [PyDev plugin](http://pydev.sourceforge.net/), you'll thus avoid indentation errors, have a great editor with advances code navigation and debugging. Having OpenERP running inside PyDev is almost automatic on Linux but is way harder in Windows due to the use of native library you'll need to have properly installed. Depending on you, you might even win time running a Linux VM inside Windows in such a case, but again, that's up to you.

Here is an example debugging OpenERP with Eclipse and PyDev:
![http://magento-openerp-smile-synchro.googlecode.com/svn/wiki/openerp_debug.png](http://magento-openerp-smile-synchro.googlecode.com/svn/wiki/openerp_debug.png)

Good luck.