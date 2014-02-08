# revision 21194
# category Package
# catalog-ctan /macros/generic/navigator
# catalog-date 2011-01-26 01:17:29 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-navigator
Version:	1.0
Release:	3
Summary:	PDF features across formats and engines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/navigator
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/navigator.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/navigator.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Navigator implements PDF features for all formats (with some
limitations in ConTeXt) with PDFTeX, LuaTeX and XeTeX (i.e.
xdvipdfmx). Features include: - Customizable outlines (i.e.
bookmarks); - Anchors; - Links and actions (e.g. JavaScript or
user-defined PDF actions); - File embedding (not in ConTeXt); -
Document information and PDF viewer's display (not in ConTeXt);
and - Commands to create and use raw PDF objects. Navigator
requires texapi and yax, both version at least 1.03.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/navigator/navigator.sty
%{_texmfdistdir}/tex/generic/navigator/navigator.tex
%{_texmfdistdir}/tex/generic/navigator/t-navigator.tex
%doc %{_texmfdistdir}/doc/generic/navigator/README
%doc %{_texmfdistdir}/doc/generic/navigator/navigator-doc.pdf
%doc %{_texmfdistdir}/doc/generic/navigator/navigator-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754250
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719103
- texlive-navigator
- texlive-navigator
- texlive-navigator
- texlive-navigator

