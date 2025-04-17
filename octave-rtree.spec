%global octpkg rtree

Summary:	An Octave native extension implementing the R-tree spatial index of Guttman-Gre
Name:		octave-rtree
Version:	0.8.2
Release:	1
License:	MIT
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/rtree/
Url:		https://gitlab.com/jjg/librtree-octave
#Source0:	https://gitlab.com/jjg/librtree-octave/-/archive/v%{version}/librtree-octave-v%{version}.tar.bz2
Source0:	https://gitlab.com/jjg/librtree-octave/-/package_files/121124775/download

BuildRequires:  octave-devel >= 6.0.0
BuildRequires:  pkgconfig(jansson)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
An Octave native extension implementing the R-tree spatial index of 
Guttman-Green. The code is an embedded version of librtree.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

