Summary:	HTML5 Generation: Fast, Pure Python, No Dependencies
Summary(pl.UTF-8):	Generowanie HTML5: szybkie, w czystym Pythonie, bez zależności
Name:		python3-html5tagger
Version:	1.3.0
Release:	1
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/html5tagger/
Source0:	https://files.pythonhosted.org/packages/source/h/html5tagger/html5tagger-%{version}.tar.gz
# Source0-md5:	5f2b0c139ecd9d00f314e9c8c2ad99b3
URL:		https://pypi.org/project/html5tagger/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With html5tagger, you can safely and quickly generate HTML5 without
any dependencies, making it the perfect solution for developers who
value speed and simplicity. And with its pure Python implementation,
you'll never have to worry about compatibility issues or adding extra
libraries to your project.

%description -l pl.UTF-8
Przy użyciu modułu html5tagger można bezpiecznie i szybko generować
HTML5 bez żadnych zależności, co jest dobrym rozwiązaniem dla
programistów caniących szybkość i prostotę. Dzięki czysto pythonowej
implementacji nie trzeba się martwić o kwestie kompatybilności czy
dodatkowe biblioteki w projekcie.

%prep
%setup -q -n html5tagger-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/html5tagger
%{py3_sitescriptdir}/html5tagger-%{version}-py*.egg-info
