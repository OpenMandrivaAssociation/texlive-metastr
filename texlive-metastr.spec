%global tl_name metastr
%global tl_revision 74751

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.3
Release:	%{tl_revision}.1
Summary:	Store and compose strings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/metastr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metastr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metastr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metastr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a package to store and compose strings in a structured way. This
can serve various purposes, for example: manage and write document
metadata; use templates for formatting document data; assist in
assembling and displaying document license information; facilitate basic
internationalisation and localisation.

