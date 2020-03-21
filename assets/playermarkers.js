var playerMarkers = [];
var infoWindowsArray = [];
var foundPlayerMarkers = null;
var validDimensions = ["", " - overworld", " - nether", " - end"];
var imageURL = "playermarkers/";
var defaultImage = 'player.png';
var playerIcons = [];
var realskinURL = 'https://crafatar.com/avatars/';
var markerFile = 'playerlocations.json';
var refreshRate = 1000;
var spawnX = -520;
var spawnZ = -85;
var spawnY = 64;
var customSpawn = true;

$(document).ready(function() {
  $.ajaxSetup({ cache: false });

	     setInterval(updatePlayerMarkers, refreshRate * 2);
  setTimeout(updatePlayerMarkers, refreshRate);


});

function prepareInfoWindow(infoWindow, item) {
	var playerOnline = (item.id == 4 ? "" : (item.id == 5 ? "<h3><i>offline</i></h3>" : ""))
  var c =
    "<div class=\"infoWindow\" style='width: 300px'>\
	<table><tr><td><img src='" + getIcon(item,72) + "'/></td><td>\
    <h1>"+item.msg+"</h1>" + playerOnline + "\
    <p style='text-align: left;'>\
    X: "+item.x+"\
    &nbsp;&nbsp;Y: "+item.y+"\
    &nbsp;&nbsp;Z: "+item.z+"</p>\
	</td></tr></table>\
	</div>";
  if (c != infoWindow.getContent())
    infoWindow.setContent(c);
}

function getIcon(item, size) {
	if(size == undefined || typeof(size) == undefined || size < 16)
	{
		size = 24;
	}
     return realskinURL + item.msg + '&s=' + size;
}
var controlDiv;
var playerDdl;
var offlineChk;

function playerDropDown() {
	if(controlDiv == null || controlDiv == undefined)
	{
	  controlDiv = document.createElement('div');
      $(controlDiv).attr('id','controlDiv');
	  $(controlDiv).attr('class','customControl');
      overviewer.map.controls[google.maps.ControlPosition.TOP_RIGHT].push(controlDiv);
	  playerDdl = document.createElement('select');
	  var select_html = '<select><option selected value="no"> - Follow a player - <\/option>';
	  select_html += '<\/select>';
      $(playerDdl).html(select_html);

	  $(playerDdl).attr('id','ddlFollowPlayer');
	  var checkOffline_html = '<input id="chkOfflinePlayer" type="checkbox" value="true" \/> <span style="background-color: rgba(0,0,0,0.5);color: #ffffff;">Show offline players</span>';

	  $(controlDiv).html($(playerDdl));
	  $(controlDiv).append(checkOffline_html);
	}

        for (player in playerMarkers) {
			var playerName = playerMarkers[player].title.replace(" - offline", "").replace("offline", "");
			var playerId = "player_" + playerName;
			if($('#controlDiv option[id="' + playerId + '"').length < 1)
			{
				$(playerDdl).append('<option id="' + playerId + '" value="'+playerName+'">'+ playerName +'</option>');
			}

        }


}

function updatePlayerMarkers() {
	  overviewer.collections.spawnMarker.setPosition(overviewer.util.fromWorldToLatLng(spawnX, spawnY, spawnZ, overviewer.mapView.options.currentTileSet));

	playerDropDown();
  var playerInfoURL = markerFile + '?' + Math.round(new Date().getTime());
  $.getJSON(playerInfoURL, function(data) {
    var foundPlayerMarkers = [];
    for (i in playerMarkers)
      foundPlayerMarkers.push(false);

    var curWorld = overviewer.mapView.options.currentTileSet.attributes.world.id;
    for (i in data) {
      var item = data[i];
      if(item.id != 4 && item.id != 5) continue; // 4=online, 5=offline, 6=sneaking, 7=invisible, 8=spectator

      var onCurWorld = false;
      for (var i=0; i<validDimensions.length; i++) {
        if (item.world.toUpperCase() + validDimensions[i].toUpperCase() == curWorld.toUpperCase()) {
          onCurWorld = true;
          break;
        }
      }
      if (!onCurWorld) continue;

      var converted = overviewer.util.fromWorldToLatLng(item.x, item.y, item.z, overviewer.mapView.options.currentTileSet);
      var playerOnline = (item.id == 4 ? "" : (item.id == 5 ? " - offline" : ""))

      //if found, change position
      var found = false;
	  var showOffline = $(chkOfflinePlayer).is(":checked");
      for (player in playerMarkers) {
        if(playerMarkers[player].getTitle() == item.msg + playerOnline) {
          foundPlayerMarkers[player] = found = true;
          playerMarkers[player].setPosition(converted);
		  //playerMarkers[player].setIcon(imageURL+'?'+playerOnline+"?small?"+item.msg);
          playerMarkers[player].setIcon(getIcon(item));

		  if(item.id == 4 || showOffline) {
			if(playerMarkers[player].getMap() == null) {
			   playerMarkers[player].setMap(overviewer.map);
			}
		  }
		  else{
		    playerMarkers[player].setMap(null);
		  }
		  if($('#ddlFollowPlayer').val() == item.msg) {
		    overviewer.map.panTo(converted);
		  }
          prepareInfoWindow(infoWindowsArray[player], item);
          break;
        }
      }
      //else new marker
      if(!found) {
        var marker =  new google.maps.Marker({
          position: converted,
          map: overviewer.map,
          title: item.msg + playerOnline,
		  //icon: imageURL+'?'+playerOnline+"?small?"+item.msg,
          icon: getIcon(item),
          visible: true,
          zIndex: 999
        });
        playerMarkers.push(marker);

        var infowindow = new google.maps.InfoWindow({content: item.msg});
        prepareInfoWindow(infowindow, item);
        google.maps.event.addListener(marker, 'click', function(event) {
          var i = 0;
          for (playerindex in playerMarkers) {
            if (playerMarkers[playerindex].title == this.title) {
              i = playerindex;
              break;
            }
          }
          if(infoWindowsArray[i].getMap()){
            infoWindowsArray[i].close()
          } else {
            infoWindowsArray[i].open(overviewer.map, playerMarkers[i]);
          }
        });
        infoWindowsArray.push(infowindow);
        foundPlayerMarkers.push(true);
      }
    }

    //remove unused markers
    for (i in playerMarkers) {
      if (!foundPlayerMarkers[i]) {
        playerMarkers[i].setMap(null);
      }
    }



  });
}
