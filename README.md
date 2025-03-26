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

# Database models
1. User - item budget?
2. Item - contains description of item, and also rules for stewardship changes (e.g. how long the stewardship change lockout is, how many budget points this item consumes?)
3. StewardshipRecord - new record created when an item changes hands, and maintains information about the item's condition, such as location. also contains use case (could be transfered to use the item, or perform maintenance, or to store the item.) - use what 3 words api?
4. StewardReport - attached to Stewardship records, noting things like item condition upon taking custody, unexpected breaking, etc.
5. Certification - acknowledgements of skill or training in specific areas, e.g. ability to use a 3d printer, drive a vehicle, or use a chainsaw. Also provide user permissions, such as being a system admin or a moderator.
6. ItemCertRequirement - what certifications a user needs to have before an item can transfer to their stewardship. can have different requirements for different stewardship types. Join table
7. UserCertification - a token marking completion of a certification. always has a lifetime, or can be taken away through disciplinary action. Join table.
8. MaintenanceRequirement - attached to items to determine how often and what sort of care they require.
9. MaintenanceLog - record of actual maintenance performed on items.
10. Tag
11. ItemTags - join table
12. CertificationTag? - default cert requirements that come from tags?
13. MaintenanceTag? - default maintenance requirements that come from tags?
14. NodeSettings - EAV table for stuff like default user item budget, Node name and ID, etc.? 
15. PeerAssesment - records of both peer punishments and peer commendations. Altruistic punishment is accomplished by requiring multiple other users to give up their certification(s) to remove an equivalent certification of the target user. How to handle peer rewards? also how certifications are bestowed?
16. Post - Necessary? Way to build community. Pinnable to show rules? Instructions? longer form content.
17. Thread - Way to request and coordinate, uses location like in foxhole game. short form content.