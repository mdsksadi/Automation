import customtkinter as ctk
from customtkinter import ttk

''' 
A singleton class for managing the main application window. 
This class ensures that only one instance of the main window exists throughout the application lifecycle. 
'''

class SingletonFrame(ctk.CTk):
    _instance = None
    _scrollbar = None
    _canvas = None
    _scrollable_frame = None
    _frame = None
    
    ''' 
    Returns the singleton instance of the main application window.
    If the instance does not exist, it creates one. 
    '''
    @staticmethod
    def get_instance():
        if SingletonFrame._instance is None:
            SingletonFrame()
        return SingletonFrame._instance
    
    '''
    Creates the main application window and initializes its components. 
    Args:
        title (str): The title of the window. Default is "ErgoPulse".
        geometry (str): The size and position of the window. Default is "800x600".
    '''
    @clsassmethod
    def create_instance(cls, title="ErgoPulse", geometry="800x600"):
        # Create the singleton instance if it doesn't exist
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.title(title)
            cls._instance.geometry(geometry)
            cls._instance.configure(bg="#1E1E1E")
            
            # Create a canvas and a scrollbar for scrolling content
            cls._canvas = ctk.CTkCanvas(cls._instance, bg="#1E1E1E", highlightthickness=0)
            cls._scrollbar = ttk.Scrollbar(cls._instance, orient="vertical", command=cls._canvas.yview)
            cls._scrollable_frame = ctk.CTkFrame(cls._canvas, bg="#1E1E1E")
            
            # Configure the canvas to use the scrollbar
            cls._canvas.configure(yscrollcommand=cls._scrollbar.set)
            
            # Place the canvas and scrollbar in the window
            cls._canvas.pack(side="left", fill="both", expand=True)
            cls._scrollbar.pack(side="right", fill="y")
            
            # Create a window inside the canvas to hold the scrollable frame
            cls._canvas.create_window((0, 0), window=cls._scrollable_frame, anchor="nw")
            
            # Update the scroll region when the size of the scrollable frame changes
            cls._scrollable_frame.bind(
                "<Configure>",
                lambda e: cls._canvas.configure(
                    scrollregion=cls._canvas.bbox("all")
                )
            )
            
            # Bind mouse wheel events to enable scrolling
            cls._canvas.bind_all("<MouseWheel>", cls._on_mousewheel)
    
    