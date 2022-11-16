Name:		texlive-metastr
Version:	56246
Release:	1
Summary:	Store and compose strings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/metastr
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metastr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metastr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metastr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a package to store and compose strings in a structured
way. This can serve various purposes, for example: manage and
write document metadata; use templates for formatting document
data; assist in assembling and displaying document license
information; facilitate basic internationalisation and
localisation.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/metastr
%{_texmfdistdir}/tex/latex/metastr
%doc %{_texmfdistdir}/doc/latex/metastr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
