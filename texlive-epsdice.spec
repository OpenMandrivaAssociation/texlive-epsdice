# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/epsdice
# catalog-date 2007-02-15 14:08:03 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-epsdice
Version:	2.1
Release:	1
Summary:	A scalable dice "font"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epsdice
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsdice.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The epsdice package defines a single command \epsdice that
takes a numeric argument (in the range 1-6), and selects a face
image from a file that contains each of the 6 possible die
faces. The graphic file is provided in both Encapsulated
PostScript and PDF formats.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
