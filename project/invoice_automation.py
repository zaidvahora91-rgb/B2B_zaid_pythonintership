import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")


st.title("Invoice Automation System")
