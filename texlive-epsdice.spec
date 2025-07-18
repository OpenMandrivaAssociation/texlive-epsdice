Name:		texlive-epsdice
Version:	15878
Release:	2
Summary:	A scalable dice "font"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/epsdice
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
