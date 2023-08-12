import speech_recognition as sr
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


class SpeechBussiness():
    def __init__(self):
        self.monthly_investment:float = 0.0
        self.apr:float = 0.0
        self.years:int = 0
    
    def calculateFutureValue(self):
        monthly_interest_rate = self.apr / 100 / 12
        months = self.years * 12

        fv = 0
        for _ in range(months):
            fv += self.monthly_investment
            monthly_interest_amount = fv * monthly_interest_rate
            fv += monthly_interest_amount
        return fv


