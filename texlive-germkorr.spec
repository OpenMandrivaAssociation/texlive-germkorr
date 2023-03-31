Name:		texlive-germkorr
Version:	15878
Release:	2
Summary:	Change kerning for german quotation marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/germkorr
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package germcorr has to be loaded after the package german.
It brings some letters like T nearer to german single and
double quotes even when that letter wears a standard accent
like "`\.T"'.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/germkorr/germkorr.sty
%doc %{_texmfdistdir}/doc/latex/germkorr/COPYING
%doc %{_texmfdistdir}/doc/latex/germkorr/README
%doc %{_texmfdistdir}/doc/latex/germkorr/germkorr.pdf
%doc %{_texmfdistdir}/doc/latex/germkorr/germkorr.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
