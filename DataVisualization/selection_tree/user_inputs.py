
def retrieve():
    #This is where the user provides the .csv file with the data
    file = input("\n\tFile path: ")

    #This is where the user chooses which charts he/she wants to be computed
    graphs = ['line', 'scatter', 'bar', 'pie']
    for t in graphs:
        print(f"\n\t{graphs.index(t)} - {t.upper()}")
    types = [int(i) for i in input("\n\n\tType the indexes of the graphs you want separated by a comma (e.g. '0,1,3'): ").split(",")]

    #This is where the palette is provided
    palette = input("\n\tPalette type: ")
    return file, types, palette

if __name__ == '__main__':
    main()
