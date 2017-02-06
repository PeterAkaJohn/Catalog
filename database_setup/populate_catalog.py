from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('postgresql://catalog:catalog@localhost:5432/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

category1 = Category(user_id=1, name="Music")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Item1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id felis id, euismod pulvinar lectus. Nunc ac blandit dolor. Aenean auctor eu augue eu tempus. Duis sed molestie mauris. Fusce non nisl a felis tempor aliquam. Sed in tortor in ex consequat luctus et vitae sapien. Vestibulum vitae elementum sapien.",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category1, upvote=1, downvote=0)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Item2", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category1, upvote=2, downvote=0)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Item3", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$5.50", picture="http://lorempixel.com/400/200", category=category1, upvote=0, downvote = 1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$5.50", picture="http://lorempixel.com/400/200", category=category1, upvote=0, downvote=0)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$5.50", picture="http://lorempixel.com/400/200", category=category1, upvote=4, downvote = 0)

session.add(item5)
session.commit()

item5 = Item(user_id=1, name="Item5", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$5.50", picture="http://lorempixel.com/400/200", category=category1, upvote=3, downvote = 0)

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Item6", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$5.50", picture="http://lorempixel.com/400/200", category=category1, upvote=0, downvote = 0)

session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Item7", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$5.50", picture="http://lorempixel.com/400/200", category=category1, upvote=0, downvote = 0)

session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Item8", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$5.50", picture="http://lorempixel.com/400/200", category=category1, upvote=0, downvote = 0)

session.add(item8)
session.commit()

category2 = Category(user_id=1, name="Mountain")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Item1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id felis id, euismod pulvinar lectus. Nunc ac blandit dolor. Aenean auctor eu augue eu tempus. Duis sed molestie mauris. Fusce non nisl a felis tempor aliquam. Sed in tortor in ex consequat luctus et vitae sapien. Vestibulum vitae elementum sapien.",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category2, upvote=1, downvote=0)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Item2", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Item3", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item5)
session.commit()

item5 = Item(user_id=1, name="Item5", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Item6", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Item7", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Item8", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category2, upvote=2, downvote=0)

session.add(item8)
session.commit()

category3 = Category(user_id=1, name="PC")

session.add(category3)
session.commit()

item1 = Item(user_id=1, name="Item1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id felis id, euismod pulvinar lectus. Nunc ac blandit dolor. Aenean auctor eu augue eu tempus. Duis sed molestie mauris. Fusce non nisl a felis tempor aliquam. Sed in tortor in ex consequat luctus et vitae sapien. Vestibulum vitae elementum sapien.",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Item2", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category3, upvote=2, downvote=0)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Item3", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item5)
session.commit()

item5 = Item(user_id=1, name="Item5", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Item6", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Item7", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Item8", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category3, upvote=1, downvote=0)

session.add(item8)
session.commit()

category4 = Category(user_id=1, name="Mountain")

session.add(category4)
session.commit()

item1 = Item(user_id=1, name="Item1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id felis id, euismod pulvinar lectus. Nunc ac blandit dolor. Aenean auctor eu augue eu tempus. Duis sed molestie mauris. Fusce non nisl a felis tempor aliquam. Sed in tortor in ex consequat luctus et vitae sapien. Vestibulum vitae elementum sapien.",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Item2", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$2.99", picture="http://lorempixel.com/400/200", category=category4, upvote=2, downvote=0)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Item3", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Item4", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item5)
session.commit()

item5 = Item(user_id=1, name="Item5", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Item6", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Item7", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Item8", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut justo mi, lacinia id fe",
                     price="$7.50", picture="http://lorempixel.com/400/200", category=category4, upvote=1, downvote=0)

session.add(item8)
session.commit()

print "added categories and items!"
