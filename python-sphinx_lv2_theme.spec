%define	pyname sphinx_lv2_theme

Summary:		A minimal pure-CSS theme for Sphinx
Name: 		python-%{pyname}
Version:		1.4.6
Release:		1
License:		ISC
Group:	Development/python
Url:		https://gitlab.com/lv2/sphinx_lv2_theme
Source0:        https://gitlab.com/lv2/sphinx_lv2_theme/-/archive/v%{version}/%{pyname}-v%{version}.tar.bz2
BuildRequires:		python
BuildRequires:		python-setuptools
BuildRequires:		python-setuptools_scm
BuildRequires:		python-sphinx
#BuildRequires:	pkgconfig(python3)
BuildArch:		noarch

%description 
This is a minimal pure-CSS theme for Sphinx that uses the documentation style
of the LV2 plugin specification and related projects. This theme is geared
toward producing beautiful API documentation for C, C++, and Python that is
documented using the standard Sphinx domains.

%files
%doc README.md
%license LICENSE
%{py_puresitedir}/%{pyname}
%{py_puresitedir}/%{pyname}-%{version}-py%{pyver}.egg-info

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{pyname}-v%{version}


%build
%py_build


%install
%py_install
