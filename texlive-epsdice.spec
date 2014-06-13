# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/epsdice
# catalog-date 2007-02-15 14:08:03 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-epsdice
Version:	2.1
Release:	7
Summary:	A scalable dice "font"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epsdice
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The epsdice package defines a single command \epsdice that
takes a numeric argument (in the range 1-6), and selects a face
image from a file that contains each of the 6 possible die
faces. The graphic file is provided in both Encapsulated
PostScript and PDF formats.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/epsdice/dice.eps
%{_texmfdistdir}/tex/latex/epsdice/dice.pdf
%{_texmfdistdir}/tex/latex/epsdice/epsdice.cfg
%{_texmfdistdir}/tex/latex/epsdice/epsdice.sty
%doc %{_texmfdistdir}/doc/latex/epsdice/README
%doc %{_texmfdistdir}/doc/latex/epsdice/dice.eps
%doc %{_texmfdistdir}/doc/latex/epsdice/dice.pdf
%doc %{_texmfdistdir}/doc/latex/epsdice/epsdice.pdf
#- source
%doc %{_texmfdistdir}/source/latex/epsdice/epsdice.dtx
%doc %{_texmfdistdir}/source/latex/epsdice/epsdice.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 751496
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 718348
- texlive-epsdice
- texlive-epsdice
- texlive-epsdice
- texlive-epsdice

