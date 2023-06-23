### Official [APIs](https://develop.battle.net/documentation/world-of-warcraft)

This file provides documentation and examples for accessing various APIs related to the game World of Warcraft.

Below is what you can already use in your projects!

### [Game Data](https://develop.battle.net/documentation/world-of-warcraft/game-data-apis)


- Achievement
  - Achievement Categories Index: Returns an index of achievement categories.
  - Achievement Category: Returns an achievement category by ID.
  - Achievements Index: Returns an index of achievements.
  - Achievement: Returns an achievement by ID.
  - Achievement Media: Returns media for an achievement by ID.


- Auction House
  - Auctions: Returns all active auctions for a connected realm.
  - Commodities: Returns all active auctions for commodity items for the entire game region.


- Connected Realm
  - Connected Realms Index: Returns an index of connected realms.
  - Connected Realm: Returns a connected realm by ID.
  - Connected Realms Search: Performs a search of connected realms.


- Creature
  - Creature Families Index: Returns an index of creature families.
  - Creature Family: Returns a creature family by ID.
  - Creature Types Index: Returns an index of creature types.
  - Creature Type: Returns a creature type by ID.
  - Creature: Returns a creature by ID.
  - Creature Search: Performs a search of creatures. The fields below are provided for example.
  - Creature Display Media: Returns media for a creature display by ID.
  - Creature Family Media: Returns media for a creature family by ID.


## [Profile](https://develop.battle.net/documentation/world-of-warcraft/profile-apis)


- Character Achievements
  - Character Achievements Summary: Returns a summary of the achievements a character has completed.
  - Character Achievement Statistics: Returns a character's statistics as they pertain to achievements.


- Character Appearance
  - Character Appearance Summary: Returns a summary of a character's appearance settings.


- Character Collections
  - Character Collections Index: Returns an index of collection types for a character.
  - Character Mounts Collection Summary: Returns a summary of the mounts a character has obtained.
  - Character Pets Collection Summary: Returns a summary of the battle pets a character has obtained.
  - Character Toys Collection Summary: Returns a summary of the toys a character has obtained.
  - Character Heirlooms Collection Summary: Returns a summary of the heirlooms a character has obtained.


- Character Encounters
  - Character Encounters Summary: Returns a summary of a character's encounters.
  - Character Dungeons: Returns a summary of a character's completed dungeons.
  - Character Raids: Returns a summary of a character's completed raids.


- Character Equipment
  - Character Equipment Summary: Returns a summary of the items equipped by a character.


- Character Hunter Pets
  - Character Equipment Summary: If the character is a hunter, returns a summary of the character's hunter pets. Otherwise, returns an HTTP 404 Not Found error.
