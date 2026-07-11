%global tl_name germkorr
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Change kerning for German quotation marks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/germkorr
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package germcorr has to be loaded after the package german. It
brings some letters like T nearer to german single and double quotes
even when that letter wears a standard accent like "`\.T"'.

