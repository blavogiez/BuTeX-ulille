# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

BuTeX is a LaTeX document class system for creating professional academic and technical reports. The project provides customized LaTeX classes (`butexFR.cls` and `butexEN.cls`) with French and English language support, featuring modern typography, code highlighting, mathematical environments, and professional formatting.

## Repository Structure

```
BuTeX/
├── rapport/                    # Main LaTeX project directory
│   ├── butexFR.cls            # French LaTeX class file (main)
│   ├── butexEN.cls            # English LaTeX class file
│   ├── butexFR-defaultfont.cls # French class with default fonts
│   ├── test.tex               # Example/test document
│   ├── img/                   # Image assets
│   ├── logos/                 # Logo assets
│   ├── *.cache/               # LaTeX build cache directories
│   └── test.*                 # Generated LaTeX auxiliary files
```

## Build Process

### LaTeX Compilation
- **Primary command**: `pdflatex test.tex` (run from `rapport/` directory)
- **Full build process** (for documents with nomenclature/bibliography):
  1. `pdflatex test.tex`
  2. `makeindex test.nlo -s nomencl.ist -o test.nls` (if using nomenclature)
  3. `pdflatex test.tex` (second pass)
  4. `pdflatex test.tex` (third pass for cross-references)

### Required LaTeX Packages
The classes require these LaTeX packages to be installed:
- `babel` (with french/english support)
- `minted` (for code highlighting - requires Python pygments)
- `tcolorbox`, `tikz`, `pgfplots`
- `booktabs`, `multirow`, `longtable`, `colortbl`
- `siunitx`, `amsmath`, `mathtools`
- `hyperref`, `nomencl`, `subcaption`

## LaTeX Class Architecture

### Core Features
- **Language variants**: `butexFR.cls` (French) and `butexEN.cls` (English)
- **Typography**: Professional fonts with microtype optimization
- **Color scheme**: Corporate color palette with semantic colors for different content types
- **Code highlighting**: Language-specific syntax highlighting via minted/listings
- **Mathematical environments**: Enhanced theorem, definition, example, and remark boxes
- **Information boxes**: Styled boxes for results, comparisons, observations, and warnings

### Key Commands and Environments
- Document metadata: `\titre{}`, `\UE{}`, `\sujet{}`, `\enseignant{}`, `\eleves{}`
- Page generation: `\fairepagedegarde`, `\fairemarges`, `\tabledematieres`
- Information boxes: `\info{}`, `\res{}`, `\comp{}`, `\obs{}`, `\warning{}`
- Code environments: `\begin{codeboxlang}{language}...\end{codeboxlang}`
- Figure insertion: `\insererfigure{path}{width}{caption}{label}`
- Mathematical environments: `theorem`, `definition`, `exemple`, `remarque`

### Font System
The English class (`butexEN.cls`) includes a flexible font selection system:
- `\policeprincipale{fontname}` - Select main font (times, palatino, mathptmx, etc.)
- `\policesecondaire{fontname}` - Select secondary font

### Color System
Professional color palette defined in both classes:
- Primary colors: `primary`, `secondary`, `accent`
- Semantic colors: `success`, `warning`, `error`
- Content-specific colors: `resultcolor`, `comparisoncolor`, `observationcolor`, `attentioncolor`
- Language-specific code colors: `pythonframe`, `javaframe`, `sqlframe`, etc.

## Working with This Project

### Making Changes to Classes
1. Edit the appropriate `.cls` file (`butexFR.cls` or `butexEN.cls`)
2. Test changes using `test.tex` as the example document
3. Recompile with `pdflatex test.tex` to verify formatting

### Testing Documents
- Use `test.tex` as a comprehensive example showing all class features
- The test document demonstrates: typography, mathematics, code blocks, figures, tables, information boxes, and cross-references
- Generated PDF shows the visual output of all class styling

### Cache and Build Artifacts
- LaTeX generates numerous auxiliary files (`.aux`, `.log`, `.toc`, etc.)
- Cache directories (`*.cache/`) store build metadata and successful compilations
- Clean builds may require deleting auxiliary files: `rm *.aux *.log *.out *.toc`

### Dependencies
- **LaTeX distribution**: MiKTeX, TeX Live, or MacTeX
- **Python with pygments**: Required for `minted` code highlighting
- **Font packages**: Various LaTeX font packages depending on selected fonts

## File Naming Conventions
- Class files: `butex[LANG].cls` (e.g., `butexFR.cls`, `butexEN.cls`)
- Variants: `butex[LANG]-[variant].cls` (e.g., `butexFR-defaultfont.cls`)
- Test documents: `test.tex`, `test_[variant].tex`