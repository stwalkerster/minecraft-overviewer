worlds["world"] = "worlds/combatupdate"
outputdir = "maps/combatupdate"

stw_gen_nether = True
stw_gen_end = False

stw_markers = [
		dict(name="Witch Huts", filterFunction=witchHutSignFilter, icon="../icons/marker_witch.png"),
		dict(name="Temples", filterFunction=templeSignFilter, icon="../icons/temple-2.png"),
		dict(name="Houses", filterFunction=houseSignFilter, icon="../icons/marker_house.png", checked="true"),
		dict(name="Towns", filterFunction=townSignFilter, icon="../icons/marker_town.png", checked="true"),
		dict(name="Portals", filterFunction=portalSignFilter, icon="../icons/marker_portal.png", checked="true"),
		dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="../icons/treasure-mark.png", checked="true"),
		dict(name="Minecart Station", filterFunction=trainSignFilter, icon="../icons/marker-train.png", checked="true"),
		dict(name="Dock", filterFunction=dockSignFilter, icon="../icons/harbor.png", checked="true"),
		dict(name="Canal", filterFunction=canalSignFilter, icon="../icons/taxiboat.png", checked="true"),
		dict(name="Spawners", filterFunction=spawnerFilter, icon="../icons/zombie-outbreak1.png", checked="false"),
		dict(name="Mines", filterFunction=mineSignFilter, icon="../icons/mine.png", checked="true"),
		dict(name="Farming: Fields", filterFunction=fieldSignFilter, icon="../icons/field.png", checked="true"),
		dict(name="Farming: Enclosures", filterFunction=enclosureSignFilter, icon="../icons/enclosure.png", checked="true"),
		dict(name="Huts", filterFunction=hutFilter, icon="../icons/bunker-2-2.png", checked="true"),
		dict(name="Igloos", filterFunction=iglooFilter, icon="../icons/bunker.png", checked="true"),
		dict(name="Players", filterFunction=playerFilter, checked="true"),
	]

stw_nether_markers = [
		dict(name="Nether Fast Transport", filterFunction=netherFastTransportSignFilter, icon="../icons/underground.png", checked="true"),
		dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="../icons/treasure-mark.png", checked="true"),
		dict(name="Houses", filterFunction=houseSignFilter, icon="../icons/marker_house.png", checked="true"),
		dict(name="Portals", filterFunction=portalSignFilter, icon="../icons/marker_portal.png", checked="true"),
		dict(name="Nether Fortresses", filterFunction=fortressSignFilter, icon="../icons/castle-2.png", checked="true"),
		dict(name="Spawners", filterFunction=spawnerFilter, icon="../icons/zombie-outbreak1.png", checked="false"),
		dict(name="Huts", filterFunction=hutFilter, icon="../icons/bunker-2-2.png", checked="true"),
	]

stw_end_markers = []

