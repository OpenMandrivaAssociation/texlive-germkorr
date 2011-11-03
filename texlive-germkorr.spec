# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/germkorr
# catalog-date 2009-11-10 09:15:37 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-germkorr
Version:	1.0
Release:	1
Summary:	Change kerning for german quotation marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/germkorr
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germkorr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package germcorr has to be loaded after the package german.
It brings some letters like T nearer to german single and
double quotes even when that letter wears a standard accent
like "`\.T"'.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/germkorr/germkorr.sty
%doc %{_texmfdistdir}/doc/latex/germkorr/COPYING
%doc %{_texmfdistdir}/doc/latex/germkorr/README
%doc %{_texmfdistdir}/doc/latex/germkorr/germkorr.pdf
%doc %{_texmfdistdir}/doc/latex/germkorr/germkorr.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
