# GC_Content_Calculator

## Problem Statement

Antimicrobial resistance genes, such as *gyrA* in *Salmonella Typhi*, are often
analyzed for sequence-level properties like GC content, which can affect DNA
stability, mutation rates, and how genes are studied computationally. This
tool addresses the need for a quick, reusable way to calculate GC content
directly from real gene sequence data, rather than manually computing it for
each new sequence.

## What This Tool Does

A Python tool that reads a DNA sequence from a FASTA file and calculates the
GC content (percentage of Guanine and Cytosine bases) of that sequence,
using [Biopython](https://biopython.org/) to handle real biological data
rather than hardcoded examples.

## Example Data

- **Gene used:** *gyrA*, *Salmonella Typhi*
- **Source:** NCBI GenBank, accession [ON220744](https://www.ncbi.nlm.nih.gov/nuccore/ON220744)
- **Relevance:** *gyrA* mutations are linked to fluoroquinolone resistance —
  connected to my Master's thesis research on antimicrobial resistance in
  *Salmonella typhi*.

## Requirements

- Python 3.x
- Biopython (`pip install biopython`)

## Usage

```bash
python gc_calculator.py
```

(The script currently reads `sequence.fasta` directly — make sure it's in
the same folder as the script.)

## Sample Output

Running the tool on the gyrA gene sequence produces:

```
ON220744.1
ON220744.1 Salmonella enterica subsp. enterica serovar Typhi strain JKT-B2016-1 DNA gyrase subunit A (gyrA) gene, partial cds
TCTGCCCGTGTCGTTGGTGACGTAATCGGTAAATACCATCCCCACGGCGATTCCGCAGTGTATGACACCA...
372
54.03 %
```

## How It Works

The script uses Biopython's `SeqIO.read()` to parse a single-sequence FASTA
file, then a custom `percentage_GC()` function counts the G and C bases in
the sequence and calculates their percentage of the total sequence length.