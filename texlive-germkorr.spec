# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/germkorr
# catalog-date 2009-11-10 09:15:37 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-germkorr
Version:	1.0
Release:	6
Summary:	Change kerning for german quotation marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/germkorr
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752263
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718539
- texlive-germkorr
- texlive-germkorr
- texlive-germkorr
- texlive-germkorr

