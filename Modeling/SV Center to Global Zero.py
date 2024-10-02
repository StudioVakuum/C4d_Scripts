"""
Description-US: Position and Axis of the children won't be affected
"""

import c4d

def ResetObjectPosition(obj):
    # Speichere die ursprüngliche Position für die Undo-Funktion
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
    
    # Speichere die globalen Matrizen aller Kindobjekte
    children_global_matrices = {}
    for child in obj.GetChildren():
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, child)
        children_global_matrices[child] = child.GetMg()
    
    # Setze die Matrix des Objekts auf die Identitätsmatrix (Nullpunkt)
    obj.SetMg(c4d.Matrix())
    
    # Setze die Kindobjekte auf ihre ursprünglichen globalen Positionen zurück
    for child, global_matrix in children_global_matrices.items():
        child.SetMg(global_matrix)

def main():
    doc = c4d.documents.GetActiveDocument()
    
    # Starte eine Undo-Gruppe
    doc.StartUndo()
    
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
    for obj in selected_objects:
        ResetObjectPosition(obj)
    
    # Beende die Undo-Gruppe
    doc.EndUndo()
    
    c4d.EventAdd()

if __name__ == '__main__':
    main()