from anytree import Node, RenderTree  #importamos la libreria anytree que nos servira para crear arboles


udo = Node("Udo")   #creamos la raiz de nuestro arbol ROOT
marc = Node("Marc", parent=udo)   #nodo hijo de udo
lian = Node("Lian", parent=marc)  #nodo hijo de marc
dan = Node("Dan", parent=udo)     #nodo hijo de udo
jet = Node("Jet", parent=dan)     #nodo hijo de dan
jan = Node("Jan", parent=dan)     #nodo hijo de dan
joe = Node("Joe", parent=dan)     #nodo hijo de dan

for pre, fill, node in RenderTree(udo):  #le decimos a la libreria que rellene los nodos y los ordene utilizando la raiz udo
    print("%s%s" % (pre, node.name))     #imprimimos el arbol generado a partir de la raiz udo con los nodos hijos

