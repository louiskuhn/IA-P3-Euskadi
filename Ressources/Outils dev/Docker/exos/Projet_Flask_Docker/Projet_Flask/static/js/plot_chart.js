function plot_chart(data) {
    var parser = d3.timeParse("%Y-%m-%d");
    data.forEach(function(d){ d.date = parser(d.time); });

    // Dimensions et marges
    var margin = {top: 10, right: 30, bottom: 30, left: 100},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // Ajout de svg dans le body
    console.log(d3.select("#my_dataviz").attr("width"))
    console.log(d3.select("#my_dataviz").attr("height"))
    
    var svg = d3.select("#my_dataviz")
        .append("svg")
        // .attr("width", 960 + margin.left + margin.right)
        // .attr("height", 500 + margin.top + margin.bottom)
        .attr("preserveAspectRatio", "xMinYMin meet")
        .attr("viewBox", "0 0 960 500")
    .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Liste des variables et ajout des options au bouton
    var allGroup = ["open", "high", "low", "close", "volume"]

    d3.select("#selectButton")
    .selectAll('myOptions')
        .data(allGroup)
    .enter()
        .append('option')
    .text(d => d) // texte du menu
    .attr("value", d => d) // valeur retournée par le bouton

    // Couleurs : une par variable (groupe)
    var myColor = d3.scaleOrdinal()
    .domain(allGroup)
    .range(d3.schemeSet2);
    
    // Axe X
    var x = d3.scaleTime()
    .domain(d3.extent(data, d => d.date))
    .range([ 0, width ]);
    svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

    // Axe Y
    var y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return +d.open; })])
    .range([ height, 0 ]);
    var yAxis = svg.append("g")
    .call(d3.axisLeft(y));

    // Initialize line with group a
    var line = svg
        .append('g')
        .append("path")
        .datum(data)
        .attr("d", d3.line()
            .x(function(d) { return x(+d.date) })
            .y(function(d) { return y(+d.open) })
        )
        .attr("stroke", function(d){ return myColor("open") })
        .style("stroke-width", 4)
        .style("fill", "none")

    // Fonction de mise à jour du graph en fonction de la variable sélectionnée
    function update(selectedGroup) {

        // Nouveau dataset avec la variable selectionnée
        var dataFilter = data.map(function(d){return {date: d.date, value:d[selectedGroup]} })

        // Màj de l'axe Y
        y.domain([0, d3.max(data, function(d) { return +d[selectedGroup]; })])
        yAxis.transition().duration(1000).call(d3.axisLeft(y))

        // On envoie ces nouvelles données pour màj la courbe
        line
            .datum(data)
            .transition()
            .duration(1000)
            .attr("d", d3.line()
            .x(function(d) { return x(+d.date) })
            .y(function(d) { return y(+d[selectedGroup]) })
            )
            .attr("stroke", function(d){ return myColor(selectedGroup) })
        }

        // on lance update à chaque changement de variable sélectionnée
        d3.select("#selectButton").on("change", function(d) {
            var selectedOption = d3.select(this).property("value")
            console.log(selectedOption)
            update(selectedOption)
        })
};