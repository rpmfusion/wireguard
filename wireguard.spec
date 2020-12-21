Name:           wireguard
Summary:        Fast, modern, secure VPN tunnel
Version:        1.0.20201221
Release:        1%{?dist}
License:        GPLv2

URL:            https://www.wireguard.com/
Source0:        https://git.zx2c4.com/wireguard-linux-compat/snapshot/wireguard-linux-compat-%{version}.tar.xz
BuildArch:      noarch

Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}

# Don't enforce a version for now
Requires: wireguard-tools

%description
Kmod-common part for wireguard


%prep
%autosetup -n wireguard-linux-compat-%{version}

%build
# Nothing to build


%install
# Nothing to install


%files
%doc README.md
%license COPYING

%changelog
* Mon Dec 21 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.0.20201221-1
- Update to 1.0.20201221

* Fri Jan 31 2020 Leigh Scott <leigh123linux@googlemail.com> - 0.0.20191219-2
- Fix DNS conf issue

* Fri Dec 20 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.0.20191219-1
- Release 0.0.20191219

* Thu Dec 05 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20191205-1
- Release 0.0.20191205

* Thu Dec 05 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20191127-1
- Release 0.0.20191127

* Sun Oct 13 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20191012-1
- Release 0.0.20191012

* Sun Sep 15 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.0.20190913-1
- Release 0.0.20190913

* Tue Aug 06 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190702-2
- Patch unit file to depend on systemd-resolved.service (#5325)

* Fri Jul 05 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190702-2
- Release 0.0.20190702

* Fri May 31 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190531-1
- Release 0.0.20190531

* Sat Apr 06 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190406-1
- Release 0.0.20190406

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190227-3
- Unifying spec with Lubomir Rintel's one
- Rebuilt for akmods-ostree-post scriptlet

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20190227-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190227-1
- Release 0.0.20190227

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190123-1
- Release 0.0.20190123

* Tue Dec 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181218-1
- Release 0.0.20181218

* Mon Nov 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181119-1
- Release 0.0.20181119

* Fri Nov 16 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181115-1
- Release 0.0.20181115

* Thu Oct 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181018-1
- Release 0.0.20181018

* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181007-1
- Release 0.0.20181007

* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181006-1
- Release 0.0.20181006

* Tue Sep 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20180925-1
- Release 0.0.20180925

* Sun Sep 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20180918-1
- Initial package
