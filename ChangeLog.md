# Version 1.6.10 (for Stellaris 3.14.*)

## Update by FebHare

*Prevented several wonders from being built on Penal Colonies
*Streamlined several job trigger scripts
*Added support for the [Extra Districts](https://steamcommunity.com/sharedfiles/filedetails/?id=2792270076) mod

# Version 1.6.9 (for Stellaris 3.12.*)

## Update by FebHare

*Fixed panopticon job descriptions;
*Using correct modifiers for Knights;
*Removed requisites for techs: tech_physics_3, tech_society_3 and tech_engineering_3;
*Fixed Wardens Directorate deposit giving 1 enforcer job per pop to only giving 1;
*The Forbidden City now does not add politician jobs for empires with the exalted priesthood civic (to be in line with other ruler job swapping civics).

## Additional Changes

*Fixed Metacognition Dialectics using the wrong federation weight modifier;
*Any void empire (Void Dwellers/Machines or Voidborn) can build Wonders in habitats.

# Version 1.6.8 (for Stellaris 3.10.*)

## Update by FebHare

*Fixed councilor traits with new syntax;
*Fixed usage of new leader classes for traits;
*Added inline_script to fix some Wonder building job descriptions.

## Additional fixes

*Replaced all instances of leader classes 'admiral' and 'general' with 'commander';
*Replaced all instances of leader class 'governor' with 'official'.

# Version 1.6.7 (for Stellaris 3.9.*)

## Update

*Update features to 3.9.**;
*Swapped is_orbital_ring = no for is_normal_starbase = yes;
*Fixed Titan Forge army bug;
*Counterweight Habitat now add a Major Orbital with no further bonuses.

# Version 1.6.6 (for Stellaris 3.8.*)

## Update

*Update features to 3.8.**;
*Updating leader traits to new system;
*Now using the following Merger of Rules triggers for better compatibility: merg_is_standard_empire, merg_is_default_empire, merg_is_fallen_empire, merg_is_habitat, merg_is_arcology, merg_is_machine_world, merg_is_hive_world, merg_is_hab_ringworld, merg_is_gaia, merg_is_tropical, merg_is_continental, merg_is_frozen, merg_is_ocean, merg_is_nuked, merg_is_barren, merg_is_barren_cold, merg_is_molten;
*Using custom message for flying fortress;
*Disabled Flying Fortress while there is a bug that spawns defense armies on orbit;
*Change edict length value from 0 to -1.

# Version 1.6.5 (for Stellaris 3.7.*)

## New Features

*New art exhibition event involving the MSI for Payback/Broken Shackles empires;
*New Monument of Remembrance for Afraid of the Dark or Memorialist empires (only on the homeworld);
*Memorialist, Death Cult and Reanimator empires of all kinds can now build the Unhallowed Necropolis;
*New Conduit of Unity integration for Stargazer Hives: Stargazing Orrery;
*New Enigma tech for Exploration Protocols machines: Sophistication in Simplicity;
*New events and options for Eager Explorers and Ascensionists empires;
*New bonuses for Ambitions for the new Hive Mind civics on the Solipsist Debate Hall.

## Fixes

*Workaround for adding deposits with archaeological sites that don't show up when new random minor artifacts orbital deposits are also added.

# Version 1.6.4 (for Stellaris 3.7.*)

## Update

*Version bump;
*Nerfed Monument to Synchronicity from remove job upkeep to add to country edict fund.

# Version 1.6.3 (for Stellaris 3.6.*)
## Fixes

*Now using has_planetary_wonders scripted effect to declare the mod is available;
*Now a restored Hyper Relay correctly allows for the Elevator Hyper Port to be build on the system;
*Attempted to fix crashes related to the 'Enigmatic Apotheosis' event, but I need more info to look into that.

# Version 1.6.2 (for Stellaris 3.6.*)

## Fixes

*Many modifiers were updated to use the new tradition system of Ascension paths;
*Fixed some icons not pointing to the correct effect causing some visual issues and generating error logs. Thanks for the fix, FebHare!
*Fixed a typo on Resource Wonders ai_weight values for counting generator districts so ai should be more inclined to build it where it matters and there should no longer be an error log about it. Thanks again, FebHare!
*Now the steam description shows the correct version of Stellaris (until the next update, when I'll forget it again...).

## New Features

*Added the Galactic Throne: a new development for the Forbidden City for the Galactic Sovereign.

# Version 1.6.1 (for Stellaris 3.6.*)

## Changes

*Monumentality tradition Celestial Wonders no longer adds unity when Megastructures are upgraded;
*Moved Megastructure build speed from Builder of Worlds to replace the effect and added starbase building and module build speed to builder of World;
*Changed remaining instances of pop_assembly_speed to planet_pop_assembly_mult;
*Increased special resource production from Resource Wonders;
*Limited Police State empire to only 3 Panopticons on the empire, also it now reduces 10% of empire crime instead of 20%;
*Reworked Peace Festivities/War Parades decisions to use an event interface instead of using several techs/decisions.

# Version 1.6.0 (for Stellaris 3.5.*)

## Toxoid Features

*New Living Spire designations: Mutant Spire (for Overtuned and Mutagenic Spas) and Spire of the Order (for Knights of the Toxic God);
*New Jousting Tournament (Toxic God) parade for the Martial Avenue;
*New Ceremonies of Chivalry (Toxic God) festival for the Festival Plaza;
*New Noxious Spa (Mutagenic Spa/Hyper Lubrication Basin) theme for the Nostalgia Paradise;
*New choice for peace designation on the Guardian Angel/Stellar Sentinel: Knight Outpost (Toxic God);
*New options for Relentless Industrialists on Industrial Wonders events (in the future, the devastation system will be reworked);
*Added Bath Attendant jobs (and variations) to Livings Spire/Conduit of Unity/Solipsist Debate Hall and some planetary features for Toxic Bath empires.

## New Features

*New Wonder: Feasting Grounds for Devouring Swarms and Terravores;
*Added new Living Spire designation for Subterranean Origin Empires: The Upside Down Spire;
*Added new Anomaly: Nuclear Launcher, that adds an upgrade to the Space Ramp;
*Now you can change the peace designation for the Guardian Angel/Stellar Sentinel (and reset it if it was destroyed);
*Added new choices for peace designation: Arena (for Warrior Culture), Scenic Set Piece (for Media Conglomerate) and Parade (that interacts with the Martial Avenue Wonder);
*Elevator Hyper Port can now also be built on systems with a gateway.

# Version 1.5.8 (for Stellaris 3.4.*)

## Update

*Resource Wonders now use Script Values to add jobs based on planet districts, that means they are no longer capped;
*Added support to some modded districts.

Many thanks to [MrRoAdd](https://steamcommunity.com/profiles/76561198156238638) for contributing with the code!

# Version 1.5.7 (for Stellaris 3.4.*)

## Fixes & Changes

*Multiple Guardian Harbours are now allowed on the same Orbital Ring;
*This fixes a bug where the Guardian Harbour would remove itself from construction queue.

# Version 1.5.6 (for Stellaris 3.4.*)

*Version Bump to 3.4.4!*

## New Features

*Added Korean and Japanese default English values (Japanese translation available at "[(JP localize patch) Planetary Wonders](https://steamcommunity.com/sharedfiles/filedetails/?id=2352049755)" by [FebHare](https://steamcommunity.com/profiles/76561198097877684));
*Added option to skip research events to directly obtain the Science Wonder upgrades;
*Relaxed Counterweight habitat requirements;
*Now using empire_limit for branch offices(instead of a confusing trigger).

# Version 1.5.5 (for Stellaris 3.4.*)

## New Features

*New Russian localisation!*

Thanks to [Assassin8612](https://steamcommunity.com/profiles/76561198105829369) and [Dexter Morgan](https://steamcommunity.com/profiles/76561198060299040) for the localisation!

# Version 1.5.4 (for Stellaris 3.4.*)

## New Features

*New Orbital Ring buildings: Abyssal Crater Observatory and Hyper Port;
*New Orbital Ring Module: Guardian Harbor;
*New modelling policy themed around Quantum Catapult;
*Erebus Project (and upgrade) now adds housing for the Subterranean origin;
*Added more events and options for new Overlord features.

## Balance

*Increased ai weight for specialized vassals in certain wonders.

# Version 1.5.3 (for Stellaris 3.4.*)

## Fixes

*Fixed localisation_synced.

# Version 1.5.2 (for Stellaris 3.4.* - Cepheus)

*Version Bump!*

## New Features

*New events communicating that an empire can still build un-upgraded Research Wonders after their upgrades.
*Now ethics Wonders (except the Pacifist and Militarist ones) and the Megacorp Wonder will not be destroyed when captured by an empire with another ethic (or if your ethic shifts). They will still be destroyed if Gestalts get them, still needs more work to be compatible with them.

## Balance

*Increased special project cost for research wonders upgrades;
*Astronomical Model Bureau (and upgrade) now reduces the country diplomatic upkeep and the ambition bonus makes the administrators of the planet (not country) more efficient;
*Additionally, this fixes diplomatic upkeep only applying to the planet scope, not country scope.

## Fixes

*Now every step of the Special Project for research wonders upgrade triggers the events of previous steps (preventing duplicates) to make sure all of they trigger in order;
*Prevented Drained Paradise archaeological site from spawning on any system with a megastructure (just to make sure the reward planet is useful);
*Fixed Terrace Garden event repeating for empires with the Environmentalist civic;
*Changes some modifier that were removed in 3.4;
*Correctly flipped engineering and physics requirements for science Wonders.

# Version 1.5.3 (for Stellaris 3.3.* - Libra)

## New Features

*The Unhallowed Necropolis can now be constructed on Relic Worlds;
*New events (with rewards) for completing all major developments of the Transplanetary Logistics Network and the Forbidden City.

## Balance

*Removed/Replaced/Reduced country size reduction from various sources;
*Increase buildings(Wonders, branch offices and monuments) cost, build time and upkeep (in some cases);
*Reduced bonuses granted by Wonders in general;
*Monument base no longer produces unity, Monuments unity production was reduced from 10 to 5 and cost was increased from 1000 to 1500;
*Increased most deposits upkeep;
*Increased most jobs upkeep and decreased some production;
*Streamlined and generally increased ai weight for Wonders.

## Fixes

*Fixed Wonder costing extra because they were detecting themselves on the building queue;
*Added new policy flags to each policy option (the flag name matches the option name).

# Version 1.5.2 (for Stellaris 3.3.* - Libra)

## Hotfix

*Unhallowed Necropolis now doesn't destroy itself immediately if built on a non Tomb World.

# Version 1.5.1 (for Stellaris 3.3.* - Libra)

*Version Bump!*

*Replaced Administrator jobs with Politician jobs;
*Replaced every bureaucrat job with priest for spiritualists;
*Bonuses for Bureaucrats have been replaced with bonuses for Administrators;
*Bonuses for Synapse/Evaluators consolidated on bonuses for Administrators;
*Bonuses that added Admin Cap now increase administration production (generally);
*Fixed bonuses from civics to match vanilla;
*Edicts now use the new system;
*Most Influence costs were replaced with Unity costs/upkeeps;
*Bonuses that added edict cap now add edict fund.

## New Features

*Added a new Casus Belli and War Goal to claim the Coin of Fortune.

## Fixes

*Adjusted many small values(upkeeps, costs, AI weights, etc.);
*The archaeological sites that spawn with blockers cleared will now properly spawn (I literally forgot the on_actions trigger);
*Integrated Monuments decision: Added better text explaining the effects;
*Various text corrections.

# Version 1.5.0 (for Stellaris 3.2.* - Herbert)

## New Features

*New Wonder: Department of Xenoeconomy for Megacorps;
*New Branch unique office buildings for the Department of Xenoeconomy;
*New Wonder: Nostalgia Paradise for Resort Worlds and Rogue Servitors;
*New Wonder: Unhallowed Necropolis for Tomb Worlds and Memorialist/Death cults;
*New Wonder: Blossoming Preserve for Gaia Worlds and Hive Worlds;
*New art events for recently added civics: Pompous Purists, Idyllic Bloom, Pleasure Seekers, Catalytic Processing and Master Crafters;
*Added new bonuses for recently added hive civics to the Solipsist Debate Hall;
*New archaeological sites added when blockers are cleared: Forgotten Reliquary & Hidden Factory;
*New relic found by completing the Forgotten Reliquary: The Coin of Fortune.

## Fixes

*Integrated Monuments traditions: decision enactment speed: -25% -> +25% (this was inverted as a mistake);
*Fixed Offworld Logistics Station starbase module adding trade value and collection for Gestalts, reduced energy upkeep and production;
*Fixed art event adding branch office value modifier to non-Megacorp empires;
*Fixed various jobs weights to prevent pops being turned into rulers and losing their job;
*Now using is_homicidal trigger in many places, which should increase compatibility;
*Various text corrections.

# Version 1.4.3 (for Stellaris 3.2.* - Herbert)

## Herbert Adjustments

*3.2 script language updates.
*Added the Submerged Spire designation option for aquatic empires on wet planets.
*Added Angler and Pearl Diver jobs to the Demetrius Cornucopia and Demetrius Chemical Garden for aquatic empires on wet planets.
*Added Angler and Pearl Diver jobs to the Ancient Cornucopia deposit for aquatic empires on wet planets.
*Added new event text and option for Demetrius Cornucopia for aquatic empires on wet planets.
*Remove various starbase buildings size requirements (should make them compatible with ACOT).
*Decreased Integrated Monuments influence decision cost from 150 to 75, also removed Upkeep increase and added Construction Speed bonus to the modifier.
*As a bonus, now the Integrated Monuments modifier properly display its bonus along with the custom tooltip.
*Added an extra check before adding the Holoarchive to prevent duplication.
*Corrected and adjusted many anomaly event texts (Thanks Timrath!).

# Version 1.4.2 (for Stellaris 3.1.* - Lem)

## Lem Adjustments

*Added new icons for armies;
*Ark Project deposit now increases pop growth for lithoids too;
*Decrease in habitability from Manufacturing Wonders now takes is_ideal_planet_class into account;
*Industrial Hearth now also increases artisan production of unity by 1 (because this is possible now);
*Reworked the Monumentality Ambition as a tradition (still experimenting with the concept and numbers);
*Reworked the Wonder Beyond Ambition as a permanent Edict (unlocked by finishing Monumentality);
*Now the Artifacts of the Holy Reliquary always check for the total number of traditions picked, instead of specific traditions, to determine if they can be sanctified;
*Wonders now add Catalyst Technicians or Artificers jobs if the civics are enabled;
*Edicts that increase Rare Resource production now increase minerals upkeep for jobs (since a modifier was removed).

## Fixes

*Corrected localizations;
*Improved setting of the global flag that indicates the mods presence (check for pw_active), to mirror good practices described by the Wiki.

# Version 1.4.1 (for Stellaris 3.0.*)

If you enjoy my work, have some spare money and would like to donate, now you can [url=https://ko-fi.com/namfoodle]Buy me a coffee at Ko-Fi![/url]
If you want to contribute to the translation of this mod, you can [url=https://poeditor.com/join/project?hash=CZfrmDooRh]join as a contributor at POEditor![/url]

## Fixes

*Corrected many text and tooltips (Thanks again FebHare!);
*Added new icons for rare resources in the description of some edicts;
*Corrected AI effects of the land Repurposing decision.

## Balance

*Astronomical Modeling Bureau anomaly modifier for sensors and survey now only lasts 10 years;
*Enigma Engine now can be build either on a Machine World or the capital planet;
*Solipsist Debate Hall now can be build either on a Hive World or the capital planet.

# Version 1.4.0 (for Stellaris 3.0.*)

If you enjoy my work, have some spare money and would like to donate, now you can [url=https://ko-fi.com/namfoodle]Buy me a coffee at Ko-Fi![/url]

## New Features

*Added archaeological site: Translunar Network;
*Added upgrades for each Research Wonder: [b]Interdimensional Collider[/b], [b]Psionic Observatory[/b] and [b]Metal Vivarium[/b]:
**They are unlocked by completing 3 Special Projects, representing sets of experiments;
**Each experiment set also unlocks several new techs and other bonuses along the way;
*Added new Flavor Events for the Research Wonders;
*New events for the Space Elevator;
*Added new job for Gestalts via the Space Elevator: Logistics Drone;
*Added new Commerce/Logistics policy after the 2nd Space Elevator is constructed;
*Added new Modules for the Space Elevator: Space Ramp and Skyhook:
**Space Ramp also allows for the Offworld Logistics Station Starbase Building;
**Skyhook also allows for the Starbase Skyhook Starbase Building;
*Added new decision for the Space Elevator: Moon Colony Expansion (Adding more districts and building slots);
*Added new decision for the Space Elevator: Orbital Districts Expansion (Adding more districts);
*Added new decision for the Space Elevator: Counterweight Habitat Expansion (Requires Orbital Districts and Spawns a Habitat);
*Added new decision for the Space Elevator for Galactic Community Members after the 3rd commerce resolution is passed: Open for the Galactic Market (Choose a guideline based on passed resolutions);
*Added upgrade for the Erebus Project: Erebus Fracking Plant - Also unlocks Chemical Abundance Edict;
*Added upgrade for the Helios Tower: Helios Translucent Obelisk - Also unlocks Translucent Abundance Edict;
*Added upgrade for the Demetrius Cornucopia: Demetrius Chemical Garden - Also unlocks Refinery Abundance Edict;
*Added upgrade for the Astronomical Model Bureau: Aligned Galactic Model;
*Added upgrade for the Guardian Angel: Stellar Sentinel;
*Added Special Project to eliminate devastation events from Mantle Crucible and upgrades;
*Added Special Project to further remove habitability debuff from Mantle Crucible and upgrades;
*Added new Modeling Focus Policy after the Astronomical Model Bureau is constructed (a rework of the old Expansion policy);
*Added new techs based on ethics for the Panopticon that increase its functionality and diversity of jobs;
*Added new decision for resource wonder: Land Repurposing, that allows for more resource districts for increase in district cost;
*Added new resolution for the Enigma Engine: Enigmatic Apotheosis.

## Fixes

*Added tooltips for the Holy Reliquary and Grand Archive main event options;
*Fixed Space Elevator job tooltips;
*Changed Wonders Completed notification to a custom made one;
*Changed Mantle Crucible devastation notification to a MUCH less annoying custom one;
*Astronomical Model Bureau no longer adds bureaucrats for Gestalt empires.
*Fixed Lunar Archivist Drone effect description;
*New icon for the Abyssal Crater Test Site;
*Fixed several instances where 'in' should have been 'on'.

## Balance

*Space Elevator: Base modifier now adds +5% Trade Value (Amenities for Gestalt);
*Space Elevator: Ambition modifier now adds +5% Trade Value (-5% job upkeep for Gestalt) and +5% Amenities;
*Space Elevator: +1 Merchant/Logistics Drone per 50 pops now added after researching tech (with 2 SE are build);
*Space Elevator: -50% resettlement cost bonus moved to the Space Ramp deposit;
*Space Elevator: Gestalt jobs now add: Logistics +5, Maintenance +3, Patrol +1, Synapse/Coordinator +1;
*Astronomical Model Bureau ambition bonus: Diplomacy upkeep -10%->-25%;
*Astronomical Model Bureau ambition bonus: Also reduces bureaucrat upkeep by 10%;
*Astronomical Model Bureau: Bureaucrats/Synapse Drones/Coordinators jobs per 25 pops now added after tech is researched (Expanding Bureaucracy);
*Panopticon: Decreased number of Enforcer/Telepath jobs from 8 to 5 to open design space for extra jobs from techs, based on ethics.
*Erebus Project: ambition bonus to mineral upkeep for jobs: -10% -> -15%;
*Helios Tower: ambition bonus to energy upkeep for buildings: -15% -> -20%;
*Holy Reliquary Ambition bonus: Priest jobs produces mult +50% -> +25%;
*Solipsist Debate Hall Ambition bonus for Memorialist: Chronicler Drones +1 per 50 pops -> +1.

# Version 1.3.4 (for Stellaris 3.0.*)

## New Features

*Added archaeological site: Lunar Archive;
*Added archaeological site: Living Reliquary.

## Fixes

*Fixed Stellarium event trigger that was completing the Cradle Initiative instead;
*Monumentality now adds a permanent modifier instead of increasing building slots;
*Forbidden City specific developments (for penal, resort and thrall colonies) don't show up if you don't have a planet with the designation;
*Art exhibition modifiers now are properly shown on the option tooltip (but only for the triggering planet);
*Imperious Art and Romantic Nationalism no longer add modifiers that only affect the country, instead of the planet;
**Imperious Art now adds a country modifier that increases influence production and decreases edict cost;
**Romantic Nationalism now increases the planet unity production instead of the country influence;
*Removed Tourist jobs from Space Elevator and Art Wonders for resort worlds;
*Focus modifier from the Mantle Crucible now add +5% production & upkeep for metallurgists/artisans instead of just +10% upkeep;
*Infrastructure the Transplanetary Logistic Network and Forbidden City now offer better modifiers/jobs for empires that choose the Synthetic Evolution AP;
**Medic jobs are replaced with Roboticist jobs;
**Bonus to pop growth are replaced with bonus to pop assembly;
**Bonus to habitability is not removed (for other species on the planet) but a small increase to pop assembly is added with it;
*pop_assembly_speed - > planet_pop_assembly_mult;
*Added better triggers for Grand Archive deposits.

## Wonders Beyond Ambition Changes [so far]

*Ambition upkeep: Building upkeep +50% -> Each wonder has +10 energy upkeep;
*Mantle Crucible now receives +5% production to metallurgists and artisans, regardless if they are focused or not;
*Erebus Project: +2 Mining districts -> -10% mineral upkeep for jobs;
*Helios Tower: +2 Generator districts -> -15% energy building upkeep;
*Demetrius Cornucopia: +2 Farming districts -> -15% food for pop consumption.

# Version 1.3.3 (for Stellaris 3.0.*) - Hotfix[/h1]

## Fixes

*Fixed Domed City and Abyssal Crater Test Site Empire Unique trigger;
*Correct Abyssal Test Crater for Habitats name text.

# Version 1.3.2 (for Stellaris 3.0.*)

## New Features

*Added Wonder in 4 stages: Living Spire (Unlocked by Ascension Perk for Regular Empires);
*Added Wonder in 2 stages: Conduit of Unity (Unlocked by Ascension Perk for Gestalts);
*Added Ambition: Wonders Beyond Ambitions;
*Added Industrial Hearth Tech: Integrated Industries;
*Added 5 new Enigma Techs: One With The Machine, Simultaneous Prime Analysis, Unintelligible Data Organization, Societal Overclock Regime, Simulations Within Simulations;
*Added new jobs (9 in total) for Research Wonders that provide only 1 type of research;
*Added new Secure the Omnidatabase special project;
*Added new Martial Parade: March of the Dead for Reanimated Armies;
*Added Imperial Holy Throne (For Imperial Cult): Sanctify a Holy Throne in the Holy Reliquary and upgrade the Throne Room of the Forbidden City (Thanks shadow_hunter_chris!);
*Added 10 new Anomalies related to Wonders;

## Changes & Balance

*AP Planetary Wonders now allows for multiple planetary wonders;
*AP Planetary Wonders unlocks the Living Spire for regular empires and Conduit of Unity for Gestalt;
*Resource Wonders (Helios Tower, Erebus Project & Demetrius Cornucopia) no longer require AP Planetary Wonders to be unlocked;
*Ambition Monumentality no longer requires AP Planetary Wonders;
*Ambition Monumentality now adds 1 building slot, increases planetary build speed by 50% and makes Wonders add +3 Stability;
*Reordered Edicts to make added Ambitions appear on top of other ambitions and Influence Campaigns to be after regular campaigns;
*All techs are generally more expensive and have more varied cost;
*Tech weight, cost and AI weight for techs as been standardized;
*Planetary Mega Engineering no longer requires Constructions Template (rare tech), requires Star Fortress tech;
*Planetary Mega Engineering resource capacity: +5000 -> +10000;
*Planetary Mega Engineering increase in building speed: +50% -> +25%;
*Industrial Hearth tech Urbanist Revolution housing: +25% -> +10%;
*Grand Archive tech Materialist Archiving switched area to physics from society, because physics needs some love;
*Enigma tech: Separated unity bonus from edict bonus;
*Enigma tech: Researcher bonus: +20% -> +10%;
*Enigma tech: Evaluators bonus: +20% -> +10%;
*Enigma Decipher jobs deviancy reduction: -10 -> -5;
*All Wonders are more expensive to build (+5000 base minerals) and maintain (+10 energy) if there is another wonder already on the planet;
*Resource Director/Coordinator jobs: Added CG upkeep (2), Amenities production(3) and increased resource production: +15% -> +25%;
*Resource Wonders don't have restrictions between dry, wet of cold planets anymore;
*Resource Wonders now add 1 job per district of their type (up to 15 in regular planets and 20 in Hive/Machine worlds);
*Resource Wonders produce +2 of their district type with Ambition bonus (except for habitats/RW);
*Resource Wonders decision now cost rare resources instead of energy, add devastation: +25 -> +20;
*SBH: Generally reduce number of provided jobs (to around 6 simple and 6 complex with 100 pops);
*SBH: Added small bonuses with Ambition, depending on civic (generally, +5% or -5% bonus or 1 extra job);
*Enigma Engine: Reduced provided Enigma Deciphers jobs: 10 -> 5 (still adds 1 per 25 pops);
*Enigma Engine: Changed bonus to research to depend on Ambition;
*Mantle Crucible: Reduced provided jobs: 12 -> 8 (4 Foundry/4 Artisans or 6 Foundry/2 miners);
*Mantle Crucible: Changed bonus to alloys/consumer goods to depend on Ambition AND on modifier;
*Mantle Crucible Modifier: Added upkeep cost to respective focused modifier;
*Titan Forge: Alloys jobs: 15 -> 7/8;
*Titan Forge: Alloy production bonus (+15%) attached to Ambition and upkeep increase (10%);
*Industrial Hearth: Poly Artisan jobs (base): 12 -> 6;
*Industrial Hearth: CG production bonus (+15%) attached to Ambition and upkeep increase (10%);
*Industrial Hearth: Poly-Artisan CG production: 10 -> 8; mineral upkeep: 10 -> 12;
*Research Wonders: Are now [b]Empire Unique[/b]. It makes sense mechanically and aesthetically and paves the way for a future expansion;
*Research Wonders: Adds 4 researcher and 4 specific researcher (from 12 researchers before) for their corresponding science;
*Research Wonders: science bonus increased (+10% -> +15%) and attached to Ambition;
*Grand Archive: Added bonus to reduce researcher upkeep(20%) to Ambition;
*Art Wonders: Removed priest jobs, added administrator jobs and reduced overall jobs added to around 8~9 (10~11 for upgrades);
*Art Wonders: Added amenities bonus (trade value for Megacorps) attached to Ambitions;
*Holy Reliquary: Removed culture worker jobs and reduced priest base jobs 10 -> 8;
*Holy Reliquary: Increased priest production mult (+20% -> +50%) and attached to ambition;
*Space Elevator: Reduced number of Jobs to 10 (clerks & maintenance drones), 1 Enforcer (or 2 patrol drones) and 1 Merchant;
*Space Elevator: Moved per pop Merchant/Synapse/Coordinator jobs to Ambition bonus, with amenities bonus;
*Space Elevator: Added +15% trade value bonus;
*Space Elevator: Increased Amenities bonus +10% -> +15%;
*Astronomical model Bureau: Bureaucrat jobs: 12 -> 8 and 2 Evaluator jobs for machine Intelligence;
*Astronomical model Bureau: Diplomacy Influence cost (-20% -> -10%) attached to ambition with bureaucrats per 25 pops (an expanding bureaucracy after all);
*Astronomical model Bureau: Admin cap mult: +20% -> +10%;
*Panopticon: Enforcers: 12 -> 8, Added 1 Administrator;
*Panopticon: Enforcers: Added Ambition bonus: +5% Jobs production;
*Panspectron: Enforcers: +1 per 50 pop -> +2 and decreased cost to deactivate (100 -> 50);
*Guardian Angel: Allowed in habitats with the Voidborn perk;
*Guardian Angel: Reduced soldiers jobs 7 -> 5 and enforcers 3 -> 2;
*Guardian Angel: protection from bombardment moved to Ambition bonus;
*TLN/Forbidden City: Reduced Base jobs provided to 6 (from 10) and deposits added jobs to 4(from 8);
*TLN/Forbidden City: Removed housing and amenities added, added housing multiplier to ambition bonus;
*TLN/Forbidden City: Changed a lot of the deposits, now they start with and give less bonuses overall and have debuffs applied in the form of pop/job upkeep;
*Festival Plaza: Removed Clerk, Merchant and Enforcer jobs, reduced jobs to 7 (1 Administrator, 3 Culture workers and 3 Entertainers);
*Festival Plaza: Added +10% amenities to Ambition bonus;
*Festival Plaza: Reduced happiness bonus while not at war: 25% -> 15%;
*Martial Avenue: Removed Merchant and Enforcer jobs, reduced jobs to 7 (1 Administrator, 2 Culture workers, 2 Entertainers, 2 soldiers);
*Martial Avenue: Added +10% amenities to Ambition bonus;
*Martial Avenue: Reduced happiness bonus while at war: 25% -> 15%;
*Tweaked a lot of the modifiers;

## Fixes

*Added pw_ to remaining country flags, to make sure they only affected this mod;
*Corrected a lot of wrong and weird texts (Thanks FebHare!);
*Corrected Overseers Ring not giving modifiers to thrall worlds;
*Corrected Building Priorities values to have Wonders that add Soldier/Enforcer/Patrol jobs first;
*Enigma Engine and Solipsist Debate Hall now correctly add unity modifiers when first build (instead of happiness, which did nothing);

# Version 1.3.1 (for Stellaris 3.0.2 - Hotfix)

## Fixes

* Fixed Astronomical Model Bureau recurring resource event triggering multiple times and added fail safes to make sure it does not add resources to planets that already have them.
* Fixed Grand Archive not adding assembled deposits when it is reconstructed.
* Added mechanism to periodically check if the Grand Archive is missing deposits it should have.

# Version 1.3.0 (for Stellaris 3.0.1)

## New Features

* Added Mantle Crucible;
* Added Titan Forge;
**New Titan Forge events and techs;
**New Frozen War Titan anomaly;
* Added Industrial Hearth;
**New Poly-Artisan job;
**New Industrial Hearth events and techs;
* Added Pavilion of Wonders;
**New Art Exhibition decision, events and modifiers for each ethic and some civics;
* Added Fair of Worlds (Xenophile);
**New Diversity Curator job;
* Added Museum of the Grotesque (Xenophobe);
**New Degeneracy Curator job;
* Added new Astronomical Model Bureau flavor events;
* Added new Drained Paradise archaeological site.
* Added new enigma techs (Strategic resources and housing)
* Added Holy Reliquary (Spiritualist);
**New job: Relic Keeper;
**New artifacts to sanctify, with new modifiers and effects;
* Added The Grand Archive (Materialist);
**New jobs: Grand-Archivist and Master-Archivist;
**New planetary deposits from archives;
**New techs from archives;
* Added Transplanetary Logistics Network (and Transhabitat too) (Egalitarian);
**New decisions: Develop Infrastructure;
**New planetary deposits from infrastructure;
* Added Forbidden City (Authoritarian);
**New decisions: Develop Infrastructure;
**New planetary deposits from infrastructure;
* Added Festival Plaza (Pacifist);
**New decisions: Peace Festivals;
**New Peace Stability modifiers;
* Added Martial Avenue (Militarist);
**New decisions: Martial Parades;
**New War Drive/Lust modifiers;

## Changes

* Updated to 3.0.1!
* Corrected anomaly text and options;
* Corrected resource requirements tooltips;
* Added new Erebus Project event image;
* Allowed many planet events to trigger for occupied planets.
* Changed many events to reward multiple monthly productions instead of static values.
* Reduced text in some events to fit the buttons.
* Guardian angel decisions now add planetary features, have better modifiers, proper upkeep and communicate better what they do.
* Ambitions/Campaigns/Edicts have been ordered into the right place on the list.
* Domed City Test Subject job and drone job should allow for more pops to work it while being restricted to sapient pops.
* All Wonders now have a better system to detect if an added feature should be removed, with events to explain what happened.

## Balance

* Wonder SR Cost: 100 -> 150
* Wonder Alloy Cost: 500 -> 750
* Wonder Energy Upkeep: 15 -> 20
* Wonder Stability Production (with Ambition): 5 -> 2
* Resource Increased from decision (Erebus, Demetrius, Helios): 15% -> 20%
* Resource Increased from director job (Erebus, Demetrius, Helios): 10% -> 15%
* Panopticon: Added +1 encryption.
* Panspectron: Added +1 encryption, -25% pop happiness and removed authoritarian attraction.
* Guardian Angel: decreased bombardment protection: 25% -> 10%
* Guardian Angel: Increased army starting experience: 100 -> 200
* Guardian Angel: Decreased telepath jobs: 3 -> 2
* Guardian Angel: Decreased housing (only provides housing while peace time): 3 -> 2
* Guardian Angel: Added energy upkeep to peace decisions.
* Enigma tech: worker job production: 20% -> 15%;
* Enigma tech: specialist job production: 20% -> 15%;
* Enigma tech: housing: 50% -> 20% (10% from 2 different techs);
* Enigma tech: SR production increase: 20% -> 10% (5% from 2 different techs);
* Enigma tech: Researcher and Evaluator production increase: 25% -> 20%

# Version 1.2.2 (for Stellaris 2.8.1)

## Fixes

* Fixed Solipsist Debate Hall having 1 spawning drone job per pop for devouring swarm.

# Version 1.2.1 (for Stellaris 2.8.1)

## Updates

* Update: Building icons.
* Update: event texts.

# Version 1.2.0 (for Stellaris 2.8.1)

## Changes and Fixes

* Changed: Particle Supercollider, Domed City (Secluded Sector), Abyssal Crater test Site (Planetary Test Site), Astronomical Model Bureau and Panopticon allowed in habitats with the Voidborn Ascension perk.
* Changed: Space Elevator is allowed in Resort Colonies and produces Tourist jobs.
* Added: New custom building, tech, jobs, decisions and ascension perk icons.
* Added: New event pictures for Abyssal Test Crater, Demetrius Cornucopia, Domed City, Enigma Engine, Astronomical Model Bureau, Helios Tower and Space Elevator.
* Added: New random flavor events for each wonder.
* Added: New anomalies.
* Added: Better AI Weight to wonder construction.
* Added: Tooltip for empire unique wonders.
* Changed: Corrected "Exoteric" to "Esoteric" in localization.
* Streamlined Solipsist Debate flag and edict.
* Added: Global flag 'pw_active' on game start to signalize that this mod is active.

# Version 1.1.1 (for Stellaris 2.8.1)

## Fixes

* Fixed: Big Brother job rotating pops into ruler jobs and unemployed them.
* Fixed: Criminal Heritages can get the Panopticon tech, since they can't build the Panopticon.

# Version 1.1.0 (for Stellaris 2.8.1)

## New Features

* Wonder: Astronomical Model Bureau
**Policy: Expansion (Unlocked by Astronomical Model Bureau)
* Wonder: Panopticon
**Edict: Panspectron (Unlocked by Panopticon)
* Wonder: Enigma Engine
**Techs: Enigma Techs (Unlocked by Enigma Engine)
* Wonder: Solipsist Debate Hall
**Event Chain: Solipsist Debates (Unlocked by Solipsist Debate Hall)
* New events gives Minor Artifacts to empires that lack them to build Enigma Engine and Solipsist Debate Hall.
* Wonder: Guardian Angel
**Army: Flying fortress (Unlocked by Guardian Angel)

## Changes and Fixes

* Added: Test subject/drone test subject job to Domed City
* (Which fixed a problem where Domed City would require Consumer Goods from Hive Minds)
* Restricted Domed City, Abyssal Crater Test Site and Particle Supercollider from Habitats.
**They should NOT destroy themselves, if they were already built. [strike] But that's illegal now, so you should delete them.[/strike]
* Space Elevator balance:
**Changed: 25% Immigration pull -> +20% Amenities
**Changed: -25% Resettlement Cost -> -50% Resettlement Cost
**Changed (regular): 1 Merchant -> 1 Merchant per 50 pop
**Added (hive): 1 Synapse drone per 50 pop
**Added (machine): 1 Evaluator per 50 pop
* Demetrius Fields renamed to Demetrius Cornucopia.
* Planetary Megastructures tech: added prereqfor_desc.

## Next Update Plan

* New Wonder/Tech/Decision(?) icons;
* New event pictures;
* New random events and anomalies (maybe archeological sites);
* Investigate compatibility with: PD - planetary habitats, The Belt (update) and Colonize Everything;
* Localization tools.

# Version 1.0.0 (for Stellaris 2.8.1)

**Initial Release**
Added:
* Wonder: Space Elevator
* Wonder: Particle Supercollider
* Wonder: Domed City
* Wonder: Abyssal Test Crater
* Wonder: Erebus Project
* Wonder: Helios Tower
* Wonder: Demetrius Fields
* Ascension Perk: Planetary Wonders
* Edict: (Ambition) Monumentality
