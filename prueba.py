import edges

prueba = edges.make_edge ("HasPrerequisite","/c/es/navegadorON", "/c/es/tabletON","/GSI","GSI",["/GSI/u","/GSI/l"]);
print prueba['start']
prueba2 = edges.SolrEdgeWriter('/home/alopez/temp')
prueba2.write_header()
prueba2.write(prueba)
prueba2.write_footer()

