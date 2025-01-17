import classNames from 'classnames';

export function getNavClassName({ isActive }: { isActive: boolean }) {
  return classNames('Header__navigation-list-link', {
    'navlink-active': isActive,
  });
}

export function getIconNavClassName({ isActive }: { isActive: boolean }) {
  return classNames('Header__icon', {
    'account-active': isActive,
  });
}

export function getLoginNavClassName({ isActive }: { isActive: boolean }) {
  return classNames('LoginPage__nav-link', {
    'login-navlink-active': isActive,
  });
}