Summary:	Han character dictionary
Name:		eclectus
Version:	0.2
Release:	3
Group:		Development/Python
License:	GPLv3+
URL:		http://code.google.com/p/eclectus/
Source0:	http://eclectus.googlecode.com/files/%{name}-%{version}beta.tar.gz
%py_requires -d
BuildRequires:	python-setuptools
BuildRequires:	kdelibs4-core
BuildArch:	noarch
Requires:	python-kde4
Requires:	cjklib
Suggests:	eclectus-voice-female
Suggests:	eclectus-voice-male
Suggests:	eclectus-segment-bwpng
Suggests:	eclectus-segment-ordergif
Suggests:	eclectus-segment-redpng

%description
Eclectus is a small Han character dictionary especially designed for
learners of Chinese character based languages like Mandarin Chinese
or Japanese.

%prep
%setup -qn %{name}-%{version}beta

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

%find_lang %{name}qt %{name}.lang

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


%changelog
* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.2-2mdv2011.0
+ Revision: 590791
- rebuild for py2.7

* Sat Dec 12 2009 Funda Wang <fwang@mandriva.org> 0.2-1mdv2010.1
+ Revision: 477824
- add kdecore BR
- suggests eclectus data packages
- import eclectus


