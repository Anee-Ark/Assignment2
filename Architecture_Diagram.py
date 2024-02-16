from diagrams import Diagram
from diagrams.aws.storage import S3
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Internet
from diagrams.custom import Custom


sn = r"C:\Users\devmi\Downloads\th (2).png"  # Replace with the path to your PDF files icon
txt = r"C:\Users\devmi\Downloads\th (3).png"  # Replace with the path to your CSV file icon
pdf =  r"C:\Users\devmi\Downloads\image.png"
wb =  r"C:\Users\devmi\Downloads\th (5).png"
pypdf =  r"C:\Users\devmi\Downloads\th (4).png"
cs =  r"C:\Users\devmi\Downloads\th (7).png"



with Diagram("\nArchitecture Diagram", show=False):
    internet = Internet("Website")
    scraping = Custom("Web Scraping",wb)
    Snowflake = Custom("Snowflake", sn)
    csv_file = Custom("CSV File",cs)
    pdf_files = Custom("\nPdf Files",pdf)
    docker = Server("GROBID")
    text_files = Custom("Text Files", txt)
    text_files1 = Custom("Text Files", txt)
    s3_bucket = S3("S3 Bucket")
    pypdf = Custom("PyPdf",pypdf)
    

    internet >> scraping >> csv_file >> Snowflake 
    pdf_files >> docker >> text_files >> s3_bucket >> Snowflake
    csv_file >> s3_bucket
    pdf_files >> pypdf >> text_files1 >> s3_bucket