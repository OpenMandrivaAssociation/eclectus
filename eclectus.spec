Summary:	Han character dictionary
Name:		eclectus
Version:	0.2
Release:	%mkrel 1
Group:		Development/Python
License:	GPLv3+
URL:		http://code.google.com/p/eclectus/
Source0:	http://eclectus.googlecode.com/files/%{name}-%{version}beta.tar.gz
%py_requires -d
BuildRequires:	python-setuptools
BuildArch:	noarch
Requires:	python-kde4
Requires:	cjklib
Suggests:	eclectus-voice-female
Suggests:	eclectus-voice-male
Suggests:	eclectus-segment-bwpng
Suggests:	eclectus-segment-ordergif
Suggests:	eclectus-segment-redpng
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
Eclectus is a small Han character dictionary especially designed for
learners of Chinese character based languages like Mandarin Chinese
or Japanese.

%prep
%setup -qn %{name}-%{version}beta

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot}

%find_lang %name %{name}qt

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/eclectus
%{python_sitelib}/*
%{_datadir}/applications/kde4/eclectus.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/eclectus.png
%{_iconsdir}/%{name}
%{_datadir}/pixmaps/*
