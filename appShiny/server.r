
# ################################################################################
# server.r
# 2022.09.01
# Jose ()
# version: v.1.0.beta
# Notas:
# 
# 
# ################################################################################

server <- function(input, output, session) {

  points <- reactiveVal(NULL)
  points(data.frame("lat" = c(40.4165, 37.98704, 41.38879, 37.38283, 43.37135, 43.26271),
                    "lng" = c(-3.70256, -1.13004, 2.15899, -5.97317, -8.396, -2.92528)))
  
  output$mymap <- renderLeaflet({

    map <- leaflet() %>%
            addProviderTiles(providers$Stamen.TonerLite,
                             options = providerTileOptions(noWrap = TRUE)) %>%
            addMarkers(data = points())
    
    return(map)
  })
  
  observeEvent(input$mymap_marker_click, { 
    p <- input$mymap_marker_click
    print(paste0("Latitud: ", p$lat, ", longitud: ", p$lng))
  })

  observeEvent(input$mymap_click, { 
    p <- input$mymap_click
    print(paste0("Latitud: ", p$lat, ", longitud: ", p$lng))
    
    if(!is.na(p$lat) && !is.na(p$lng) && p$lat != "" && p$lng != "" &&
       p$lat >= -90 && p$lat <= 90 && p$lng >= -180 && p$lng <= 180){
      
      pointsAnt <- points()
      points(rbind(pointsAnt, cbind("lat" = p$lat, "lng" = p$lng)))
      
      map <- leaflet() %>%
        addProviderTiles(providers$Stamen.TonerLite,
                         options = providerTileOptions(noWrap = TRUE)) %>%
        addMarkers(data = points())
    }
  })
  
  observeEvent(input$anadirPunto, {
    
    if(!is.na(input$lat) && !is.na(input$long) && input$lat != "" && input$long != "" &&
       input$lat >= -90 && input$lat <= 90 && input$long >= -180 && input$long <= 180){
      
      pointsAnt <- points()
      points(rbind(pointsAnt, cbind("lat" = input$lat, "lng" = input$long)))
      
      map <- leaflet() %>%
        addProviderTiles(providers$Stamen.TonerLite,
                         options = providerTileOptions(noWrap = TRUE)) %>%
        addMarkers(data = points())
    }
  })
  
}
