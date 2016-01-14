%global srcname ics2task
%global summary A tool to import ics events into TaskWarrior. 

Name:		python-%{srcname}
Version:	0.0.3
Release:	1%{?dist}
Summary:	%{summary}

Group:		Applications/Productivity
License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{srcname}
Source0:	http://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

%description
A tool that import ics events into tasks in TaskWarrior.
Tasks are assigned a due-date of the actual event.

%package -n python2-%{srcname}
Summary:	%{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:	python2-devel

Requires:	python-icalendar
Requires:	python-taskw

%description -n python2-%{srcname}
A tool that import ics events into tasks in TaskWarrior.
Tasks are assigned a due-date of the actual event.

%package -n python3-%{srcname}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:	python3-devel

Requires:	python3-icalendar
Requires:	python3-taskw

%description -n python3-%{srcname}
A tool that import ics events into tasks in TaskWarrior.
Tasks are assigned a due-date of the actual event.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%files -n python2-%{srcname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}*.egg-info
%{_bindir}/%{srcname}

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}*.egg-info
%{_bindir}/%{srcname}


%changelog
* Thu Jan 14 2016 Yanis Guenane <yguenane@redhat.com> 0.0.3-1
- Initial commit

