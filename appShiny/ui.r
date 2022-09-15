

ui <- fluidPage(
  leafletOutput("mymap", height=500),
  # p(),
  splitLayout(
    mainPanel(br(), numericInput("lat", "Latitud", NULL, min = -90, max = 90, width = '100px')),
    mainPanel(br(), numericInput("long", "Longitud", NULL, min = -180, max = 180, width = '100px')),
    mainPanel(br(), br(), actionButton("anadirPunto", "Añadir")))
)