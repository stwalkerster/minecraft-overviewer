renders["overworld-day-north"] = {
	"world": "world",
	"title": "Day - North",
	"rendermode": "smooth_lighting",
	"dimension": "overworld",
	"northdirection": "upper-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["overworld-night-north"] = {
	"world": "world",
	"title": "Night - North",
	"rendermode": "smooth_night",
	"dimension": "overworld",
	"northdirection": "upper-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["north-biome"] = {
	"world": "world",
	"title": "Biomes",
	"rendermode": [ClearBase(), BiomeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-north"],
	"northdirection": "upper-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["north-slime"] = {
	"world": "world",
	"title": "Slime Spawn",
	"rendermode": [ClearBase(), SlimeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-north"],
	"northdirection": "upper-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["overworld-day-south"] = {
	"world": "world",
	"title": "Day - South",
	"rendermode": "smooth_lighting",
	"dimension": "overworld",
	"northdirection": "lower-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["overworld-night-south"] = {
	"world": "world",
	"title": "Night - South",
	"rendermode": "smooth_night",
	"dimension": "overworld",
	"northdirection": "lower-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["south-biome"] = {
	"world": "world",
	"title": "Biomes",
	"rendermode": [ClearBase(), BiomeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-south"],
	"northdirection": "lower-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["south-slime"] = {
	"world": "world",
	"title": "Slime Spawn",
	"rendermode": [ClearBase(), SlimeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-south"],
	"northdirection": "lower-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["overworld-day-east"] = {
	"world": "world",
	"title": "Day - East",
	"rendermode": "smooth_lighting",
	"dimension": "overworld",
	"northdirection": "upper-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["overworld-night-east"] = {
	"world": "world",
	"title": "Night - East",
	"rendermode": "smooth_night",
	"dimension": "overworld",
	"northdirection": "upper-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["east-biome"] = {
	"world": "world",
	"title": "Biomes",
	"rendermode": [ClearBase(), BiomeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-east"],
	"northdirection": "upper-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["east-slime"] = {
	"world": "world",
	"title": "Slime Spawn",
	"rendermode": [ClearBase(), SlimeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-east"],
	"northdirection": "upper-right",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["overworld-day-west"] = {
	"world": "world",
	"title": "Day - West",
	"rendermode": "smooth_lighting",
	"dimension": "overworld",
	"northdirection": "lower-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["overworld-night-west"] = {
	"world": "world",
	"title": "Night - West",
	"rendermode": "smooth_night",
	"dimension": "overworld",
	"northdirection": "lower-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["west-biome"] = {
	"world": "world",
	"title": "Biomes",
	"rendermode": [ClearBase(), BiomeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-west"],
	"northdirection": "lower-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

renders["west-slime"] = {
	"world": "world",
	"title": "Slime Spawn",
	"rendermode": [ClearBase(), SlimeOverlay()],
	"dimension": "overworld",
	"overlay": ["overworld-day-west"],
	"northdirection": "lower-left",
	"renderchecks": "0",
	"markers": stw_markers,
}

if stw_gen_nether:
	renders["nether-north"] = {
		"world": "world",
		"title": "Nether - North",
		"rendermode": "nether_smooth_lighting",
		"dimension": "nether",
		"northdirection": "upper-left",
		"renderchecks": "0",
		"markers": stw_nether_markers,
	}
	renders["nether-south"] = {
		"world": "world",
		"title": "Nether - South",
		"rendermode": "nether_smooth_lighting",
		"dimension": "nether",
		"northdirection": "lower-right",
		"renderchecks": "0",
		"markers": stw_nether_markers,
	}
	renders["nether-east"] = {
		"world": "world",
		"title": "Nether - East",
		"rendermode": "nether_smooth_lighting",
		"dimension": "nether",
		"northdirection": "upper-right",
		"renderchecks": "0",
		"markers": stw_nether_markers,
	}
	renders["nether-west"] = {
		"world": "world",
		"title": "Nether - West",
		"rendermode": "nether_smooth_lighting",
		"dimension": "nether",
		"northdirection": "lower-left",
		"renderchecks": "0",
		"markers": stw_nether_markers,
	}

if stw_gen_end:
	renders["end-north"] = {
		"world": "world",
		"title": "The End - North",
		"rendermode": "normal",
		"dimension": "end",
		"northdirection": "upper-left",
		"renderchecks": "0",
		"markers": stw_end_markers,
	}
	renders["end-south"] = {
		"world": "world",
		"title": "The End - South",
		"rendermode": "normal",
		"dimension": "end",
		"northdirection": "lower-right",
		"renderchecks": "0",
		"markers": stw_end_markers,
	}
	renders["end-east"] = {
		"world": "world",
		"title": "The End - East",
		"rendermode": "normal",
		"dimension": "end",
		"northdirection": "upper-right",
		"renderchecks": "0",
		"markers": stw_end_markers,
	}
	renders["end-west"] = {
		"world": "world",
		"title": "The End - West",
		"rendermode": "normal",
		"dimension": "end",
		"northdirection": "lower-left",
		"renderchecks": "0",
		"markers": stw_end_markers,
	}

