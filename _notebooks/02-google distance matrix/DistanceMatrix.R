library(RJSONIO)
library(RCurl)
library(Matrix)
library(foreach)

destinationPoints <- data.frame("x"=c(8.5399366,8.5437706,8.4813986,8.4673346,8.6767616,8.4850518,8.5151529,8.5142333,8.5261612,8.7235155),"y"=c(47.3770116,47.4197246,47.4803416,47.5110986,47.3883476,47.3876176,47.3796559,47.3742395,47.385216,47.4992612))

toTimestamp <- function(date){as.numeric(as.POSIXct(date,origin="1970-01-01",tz="UTC")) }

columns <- c("originX","originY","destX","destY","bicycling","transit_w_morning","transit_w_night","transit_we","driving_peak","driving_offpeak")

# REQUEST

pointPairs <- paste(destinationPoints[,1], destinationPoints[,2], sep = ",")
points <- paste(pointPairs,collapse = "|")

departureTimesTransit <- c("transit_w_morning"=toTimestamp("2018-04-18 7:00"),"transit_w_night"=toTimestamp("2018-04-18 4:00"),"transit_we"=toTimestamp("2018-04-22 11:00"))
departureTimesDriving <- c("driving_peak"=toTimestamp("2018-04-18 7:00"),"driving_offpeak"=toTimestamp("2018-04-18 14:00"))

jsonData <- list()
#matroxData <- data.frame("")

modes <- c("bicycling","driving","transit")

travelMatrix = matrix(
  nrow=length(pointPairs)*length(pointPairs),
  ncol=length(columns),
  byrow = TRUE)

dimnames(travelMatrix) = list(c(),columns)

originXCells <- pointGridCSV[,2]
originYCells <- pointGridCSV[,3]
originPoints <- data.frame("x"=originXCells,"y"=originYCells)

steps = nrow(originPoints) %/% 25

# for(s in 1:10){
#   lowerBound = ((s-1)*25)+1
#   upperBound = s*25
#   cells <- originPoints[lowerBound:upperBound,]
#   cellPointPairs <- paste(cells[,1], cells[,2], sep = ",")
#   cellPoints <- paste(cellPointPairs,collapse = "|")
# }

# for(mode in modes){
#   if(mode == "bicycling"){
#     requestURL <- sprintf("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=%s&destinations=%s&mode=%s&key={API_KEY}", points, points, mode)
#     #print(requestURL)
#     data <- fromJSON(getURL(requestURL))
#     rows <- data[[3]]
#     for(o in seq(length(rows))){
#       for(d in seq(length(rows[[o]][[1]]))){
#         rowNumber <- (o-1)*10 + d
#         travelMatrix[rowNumber,"originX"] = destinationPoints[o,1]
#         travelMatrix[rowNumber,"originY"] = destinationPoints[o,2]
#         travelMatrix[rowNumber,"destX"] = destinationPoints[d,1]
#         travelMatrix[rowNumber,"destY"] = destinationPoints[d,2]
#         travelMatrix[rowNumber,"bicycling"] = rows[[o]][[1]][[d]][[2]][[2]]
#       }
#     }
#   }
#   else if(mode == "transit") {
#     for(i in seq(length(departureTimesTransit))){
#       time = departureTimesTransit[[i]]
#       key = names(departureTimesTransit)[i]
#       requestURL <- sprintf("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=%s&destinations=%s&mode=%s&departure_time=%s&key={API_KEY}", points, points, mode, time)
#       #print(requestURL)
#       data <- fromJSON(getURL(requestURL))
#       rows <- data[[3]]
#       for(o in seq(length(rows))){
#         for(d in seq(length(rows[[o]][[1]]))){
#           rowNumber <- (o-1)*10 + d
#           travelMatrix[rowNumber,key] = rows[[o]][[1]][[d]][[2]][[2]]
#         }
#       }
#       Sys.sleep(3)
#     }
#   }
#   else if(mode == "driving") {
#     for(i in seq(length(departureTimesDriving))){
#       time = departureTimesDriving[[i]]
#       key = names(departureTimesDriving)[i]
#       requestURL <- sprintf("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=%s&destinations=%s&mode=%s&departure_time=%s&key={API_KEY}", points, points, mode, time)
#       #print(requestURL)
#       data <- fromJSON(getURL(requestURL))
#       rows <- data[[3]]
#       for(o in seq(length(rows))){
#         for(d in seq(length(rows[[o]][[1]]))){
#           rowNumber <- (o-1)*10 + d
#           travelMatrix[rowNumber,key] = rows[[o]][[1]][[d]][[3]][[2]]
#         }
#       }
#       Sys.sleep(2)
#     }
#   }
# }

#travelMatrix