FROM continuumio/miniconda3

RUN conda install -c conda-forge ifcopenshell

ADD Duplex_A.ifc .

ADD ifc_analysis.py .

CMD ["python", "ifc_analysis.py"]

