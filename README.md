# NeighborGoods
Federated Library of Things.

This is a design document for how the Neighborhood servers should be set up in the abstract.

---
# Setup
Setup needs to be simple and intuitive requiring as little technical skill as possible. There should be a setup wizard, everything should be containerized, with step-by-step guides and walkthroughs and tutorials. Possible partnerships can be made with server hosting organizations, or public institutions for hosting to provide cheap or free server space.

# Onboarding
It should also be simple and intuitive to join. Good UI/UX design is very important here. It should be as simple as setting up a Username and Password, address and contact info, maybe a picture. Stored securely of course.

Once created, a user should be able to see the lists of posts and requests, with filters/sorting for distance, age of post, utilization, as well as a search bar with recommendations.

The user will also have the option of adding personal descriptions that are public (available to anyone on other nodes), local (anyone on this node), and private (only those you're interacting with), at their discretion. 
# Offering
A user should be able to log into their account and quickly post an item to share with the network. The item's description should include, the item's name, relevant tags, approximate price?,  a picture, a short description, and how long it can be borrowed for/if it can be borrowed off node. The owner can also offer training or help with using it if they want, along with their availability. A user can also offer services directly. including a description of what they're willing to do, and if they need tools or materials to do it.
# Requesting
A user should be able to posts requests for items or services they need/could use, including how long they need it for, and an optional description of what they are planning on doing with it. When they begin their request, the system will check the network for offers that might match the description.

# Responses
Users can respond to the posts of other users. Responders will automatically share their profile and if the poster accepts their profile will be shared. The Requester's address will then be shared for convenience and accountability. The two will meet up and the Requester will checkout the item, taking a picture of its current state (if applicable), and the Offeror will confirm that it has been handed off.

The Requestor will be reminded with automatic notifications immediately before the due date, but the item can be marked as returned by the Offeror at any time. The Requestor can also return the object by providing proof that it has been returned which will then be verified by the Offeror.
# Resolution
If the object is damaged, lost, or stolen, or a service causes damage to property, the owner should mark it as such following the interaction but the users are encouraged to resolve the dispute amongst themselves, by determining a course of action that restores or replaces the owners property or provides the owner with an item or service they deem of equal value to the repair or replacement. If the dispute cannot be resolved, or the responsible individual is unable to make restitution for whatever reason, the dispute can be mediated by the server administrator or by the community (possibly by posting a service request for a mediator). If the responsible individual does not accept moderation, the owner can request they be removed from the network node. 

All members of the community acknowledge that their property might be lost, damaged, or stolen by offering it to the community. unresolved disputes will be shown on a user's profile as part of their private description. Late returns will also be displayed for a 2 months after being resolved.

# Christian's README
NeighborGoods is a Federated Library of Things.

# Features

## Item Borrowing
A user should be able to offer items they own to the network. This includes creating a profile for the item including name, picture, description, borrowing, maintenance, and certification rules, etc. Once the object has been entered into the system, its location and stewardship is tracked, and it is displayed in a store-like list where other users can borrow it. As this is a distributed network of individuals offering up their items, there is no central repository that items must be checked in to. Instead, items are simply at the location they were last used at, until someone comes to borrow it again. Checking out an item involves clicking the borrow button, and meeting the requirements. Then, the item must transfer to the stewardship of the borrower. The current steward of the item will receive a notification that the item has been reserved for borrowing, and it is up to previous steward and the borrower how to move the item. In the future, it should be possible to have network members volunteer as gofers that move items around, but for now it's up to individual members to get their borrowed items.

Furthermore, there are different types of borrows:
- use: the item is intended to be used by the borrower
- maintenance: the item isn't going to be used, only repaired or maintained by the borrower
- restock: the item isn't going to be used, only refueled, restored, or restocked
- consume: the borrower will consume some portion of this item during the borrowing, for example, by refueling a lawnmower
- contribution: this is a special initial borrow where a user has contributed an item to the community stock
- de-list: this is a special type of borrow where a user (typically the owner or an admin) removes an item from circulation

## Certifications
Users sometimes need certification that they have specific skills or knowledge before they can borrow an item. For example, knowing how to safely handle a chainsaw before being able to use-borrow the chainsaw, or knowing how to fix two-stroke engines before being able to maintenance-borrow the chainsaw. These certs are generated by other peers in the network, either through a committee granting the cert through a collective action, or by peer assessment. A peer assessment can generate a cert by another user with the cert in question vouching for the user to receive the cert. For example, if a user with the chainsaw safety cert trains someone on proper handling of the tool, the user with the cert can choose to back the certification of the user they just taught using a peer assessment. These certs are expired by time, collective action, or by peer assessment. A peer assessment that expires a cert requires the user making the assessment to also expire their matching cert. In essence, if a user shows unsafe practices with a tool, the peer assessment is used to take the relevant cert away, at the cost of being willing to retake the cert training with the offender. These certs also provide access to administrative functions of the NeighborGoods application, such as an admin or moderator cert being required for a user to review a post.

## Collective Action
Users will sometimes need to solve the collective action problem, such as with establishing a new cert for the network, or executing on a community project. For NeighborGoods, the problem is solved using a crowd funding like procedure. When an action needs to be performed, individuals can start a collective action campaign. This campaign expires after a set amount of time, and is an all or nothing affair. If the campaign is successful, then each member must execute on their commitment. Commitments that can be performed automatically by the system are performed immediately.

## Dispute Resolution
Dispute resolution is encouraged to be done by the individuals involved, with the aid of a certified monitor.

## Posts
Posts are essentially markdown documents, with delayed publishing. All posts won't be visible to anyone besides the author and moderators until 6 am the next morning. Posts can be made in response to other posts, but this delayed pattern still holds true.

## Location Threads
These are for real-time, localized communication. They work like the map markers in foxhole, where each pin is a thread, and can have its duration extended or reduced.

## Contribution and Gamification
To help align individual incentives with pro-social actions, contributions are tracked for all users, along with how their contributions are used. These values are put into a score "leaky bucket" or moving average, so that continuous contribution towards the other network members (and by extension the network itself) is encouraged.

## The Community Currency Exchange
To facilitate the above contribution, and also alow for interfacing with the world at large, the application supports a complementary currency system, based off of the [ROCS paradigm](https://transaction.net/money/rocs/). 

## ActivityPub Integration
The eventual goal is to allow individuals to set up networks of these servers, and allow inter-node functionality for all of the above application features.

# Data Models
The following are database models that will be needed for the above system:
1. User - contains the personal information of the user, allows for authentication.
2. Item - the representation of an item
3. ItemTransfer - new record created when an item changes hands, and maintains information about the item's condition, such as location. also contains use case (could be transferred to use the item, or perform maintenance, or to store the item.) - use what 3 words api?
4. ItemLog - a simple audit log for tracking items outside of transactions. Also used to track maintenance, restock, etc.
5. Certification - acknowledgements of skill, knowledge, or training in specific areas, e.g. ability to use a 3d printer, drive a vehicle, or use a chainsaw. Also provide user permissions, such as being a system admin or a moderator.
6. ItemCertRequirement - what certifications a user needs to have before an item can transfer to their stewardship. can have different requirements for different borrow types. Join table.
7. UserCertification - a token marking completion of a certification. always has a lifetime, or can be taken away through disciplinary action. Join table.
8. MaintenanceRequirement - attached to items to determine how often and what sort of care they require.
9. Tag - a simple tagging system for items
10. ItemTags - Join table for items and tags
11. NodeSettings - An Entity Attribute Value (EAV) table that contains node specific server settings, such as item budget per person, node name, node id, collective action settings, etc.
12. PeerAssessment - records of both peer punishments and peer endorsements. One mechanism by which certs are created and removed.
13. CertAssessment - a join table between certifications and peer assessments. this join table is in part what determines which certs are active, and which are not. 
14. CollectiveActionCampaign - the record of a (possibly attempted) collective action. Can be either system external (arranging a potluck) or system internal (assigning a cert to a user, modifying node settings.)
15. CollectiveActionCert - similar to CertAssessment, this is a join table between certs and collective action campaigns, that helps determine if a cert is active or not.
16. Commitment - an individual user's commitment to a collective action campaign. Could be resources, could be a vote, etc. Once a campaign succeeds, the commitment is marked as "Outstanding", awaiting the campaign manager(s) confirmation that the commitment has been honored, or it is performed automatically (if it is a system internal campaign).
17. CampaignManager - Join table, joining users to campaigns
18. Post - a simple markdown document, with an author, and body. Can be approved / rejected by moderators.
19. PostReply - Join table, joins posts to other posts
20. CampaignReply - Join table, joins posts to Collective Action Campaigns.
21. WikiEntry - Marks the indicated post as belonging to the community wiki.
22. MapThread - Short form comments, tied to a location
23. MapThreadVote - a vote that either extends or decreases the amount of time before a map thread expires. Join table.


# Pages
The following are the available pages to interact with the application:
1. Landing - a simple page giving a high level overview of the application.
2. Login - self explanatory
3. SignUp - self explanatory
4. FAQ/About/Community Agreement - pages offering more in depth information about the platform, and this node in particular.
5. Inventory - the main page for viewing what items are available in the network, and examining them.
6. ItemManagementView - the page displays a single item in full. Also allows for borrowing.
7. ItemContribution - allows for the contribution of new items to the network.
8. UserProfile - the main page for users to manage their own profiles. Includes their own stats and history of actions involving them, along with outstanding commitments.
9. PeerAssessment - page for creating new peer assessments
10. CollectiveActionCampaigns - page that lists ongoing collective action campaigns, as well as historical ones. 
11. StartCampaign - page to start a new collective action campaign.
12. CampaignView - page that shows a collective action campaign in full.
13. Dashboard - the default page redirected to after logging in. Contains a map of the community, truncated list of collective actions, truncated list of posts, truncated list of user's outstanding commitments.
14. Feed - the untruncated list of all posts, including historical
15. PostThread - a post in full, along with other posts that respond to it.
16. Wiki - a collection of wiki posts, allowing posts to be collected into a knowledge base.

[proposed palette](https://coolors.co/palette/f0ead2-dde5b6-adc178-a98467-6c584c)
----------- 
F0EAD2
DDE5B6
ADC178
A98467
6C584C