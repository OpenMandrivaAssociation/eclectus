Summary:	Han character dictionary

Name:		eclectus
Version:	0.2
Release:	3
Group:		Development/Python
License:	GPLv3+
URL:		http://code.google.com/p/eclectus/
Source0:	http://eclectus.googlecode.com/files/%{name}-%{version}beta.tar.gz
BuildRequires:  python-devel
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
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%find_lang %{name}qt %{name}.lang

%files -f %{name}.lang
%doc COPYING README
%{_bindir}/eclectus
%{py_puresitedir}/*
%{_datadir}/applications/kde4/eclectus.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/eclectus.png
%{_iconsdir}/%{name}
%{_datadir}/pixmaps/*


