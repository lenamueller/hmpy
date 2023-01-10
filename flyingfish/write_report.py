import sys 


class Report:
    """
    Class to create a HTML report based on a description and plot for four different statistics.
    """
    
    def __init__(self, filename:str, statistics:str):

        if type not in ["Ganglinie", "Summenlinie", "Unterschreitungsdauerlinie", "Ueberschreitungsdauerlinie"]:
            sys.exit("Wrong type for class Report. Type must be 'Ganglinie', 'Summenlinie', 'Unterschreitungsdauerlinie' or 'Ueberschreitungsdauerlinie'")

        self.report_types:dict = {
            
            "Ganglinie":["Ganglinie", 
                         "text", 
                         "../images/ganglinie.png"],
            
            "Summenlinie":["Summenlinie", 
                           "text", 
                           "../images/summenlinie.png"],
            
            "Unterschreitungsdauerlinie":["Unterschreitungsdauerlinie", 
                                          "text", 
                                          "../images/unterschreitungsdauerlinie.png"],
            
            "Ueberschreitungsdauerlinie":["Überschreitungsdauerlinie", 
                                          "text", 
                                          "../images/ueberschreitungsdauerlinie.png"]
            }
        
        self.filename:str = filename
        self.header:str = ""
        self.body:str = ""

        self.heading = "<h1>"+ self.report_types[statistics][0] +"</h1>"
        self.description = "<p>" + self.report_types[statistics][1] + "</p>"
        self.image = '<img src=' + self.report_types[statistics][2] + ' height="500" >'

    def _build_head(self):
        css = f'<link rel="stylesheet" href="styles.css">'
        self.header = f"""<head>\n\t{css}\n</head>"""
        
    def _build_body(self):
        if self.heading != "" and self.image != "" and self.description != "":
            self.body = "<body>" + "\n\t" + self.heading + "\n\t<br>\n\t" + self.description + "\n\t<br>\n\t" + self.image + "\n\t<br>\n" + "</body>"
        
    def write_report(self):
        self._build_head()
        self._build_body()        

        content = f"""<html>\n{self.header}\n{self.body}\n</html>"""

        with open(f'{self.filename}','w') as f:
            f.write(content)

r = Report("report/test.html", "Ganglinie")
r.write_report()